#!/usr/bin/env python3

import argparse
import itertools
import math
import sys

from utils import save_dimacs_cnf, solve


def parse_arguments(argv):
    parser = argparse.ArgumentParser(description='Solve Sudoku problems.')
    parser.add_argument("board", help="A string encoding the Sudoku board, with all rows concatenated,"
                                      " and 0s where no number has been placed yet.")
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Do not print any output.')
    parser.add_argument('-c', '--count', action='store_true',
                        help='Count the number of solutions.')
    return parser.parse_args(argv)


def print_solution(solution):
    """ Print a (hopefully solved) Sudoku board represented as a list of 81 integers in visual form. """
    print(f'Solution: {"".join(map(str, solution))}')
    print('Solution in board form:')
    Board(solution).print()


def compute_solution(sat_assignment, variables, size):
    solution = []
    # TODO: Map the SAT assignment back into a Sudoku solution
    for i in sat_assignment:
        if sat_assignment[i] is True:
            if i%9 == 0:
                solution.append(9)
            else:
                solution.append((i%9)) 
    return solution


def grid(i, j, k):
    # Function to return data in CNF format
    return i * 81 + j * 9 + k + 1

def generate_theory(board, verbose):
    """ Generate the propositional theory that corresponds to the given board. """
    size = board.size()
    clauses = []
    variables = {}

    # TODO

    square_constraints=[]
    # One number per square
    for i, j in itertools.product(range(9), range(9)):
        square_constraints.append([grid(i, j, k) for k in range(9)])
        for k1, k2 in itertools.combinations(range(9), 2):
            square_constraints.append([str(-grid(i,j,k1)),str(-grid(i,j,k2))])

    row_constraints=[]
    # One number in one row
    for i in range(9):
        for k in range(9):
            row_numbers=[grid(i, j, k) for j in range(9)]
            row_constraints.append([str(number) for number in row_numbers])
            for j1, j2 in itertools.combinations(row_numbers, 2):
                row_constraints.append([str(-j1),str(-j2)])

    column_constraints=[]
    # One number in one column
    for j in range(9):
        for k in range(9):
            column_numbers=[grid(i, j, k) for i in range(9)]
            column_constraints.append([str(number) for number in column_numbers])
            for i1, i2 in itertools.combinations(column_numbers, 2):
                column_constraints.append([str(-i1),str(-i2)])

    block_constraints=[]
    # One number in one block or 3x3 cell
    for p, q in itertools.product(range(3), range(3)):
        for k in range(9):
            block_numbers=[grid(i, j, k) for i, j in itertools.product(range(p*3, p*3+3), range(q*3, q*3+3))]
            block_constraints.append([str(number) for number in block_numbers])
            for block_n1 in block_numbers:
                for block_n2 in block_numbers[block_numbers.index(block_n1)+1:]:
                    block_constraints.append([str(-block_n1), str(-block_n2)])

    given_info = []
    # Given information
    for i in range(len(board.data)):
        if not board.data[i] == 0:
            v = 9*i + board.data[i]
            given_info.append([str(v)])

    clauses=square_constraints+row_constraints+column_constraints+block_constraints+given_info
    variables = [i for i in range(1, 730)]

    return clauses, variables, size


def count_number_solutions(board, verbose=False):
    count = 0

    # TODO

    print(f'Number of solutions: {count}')


def find_one_solution(board, verbose=False):
    clauses, variables, size = generate_theory(board, verbose)
    return solve_sat_problem(clauses, "theory.cnf", size, variables, verbose)


def solve_sat_problem(clauses, filename, size, variables, verbose):
    save_dimacs_cnf(variables, clauses, filename, verbose)
    result, sat_assignment = solve(filename, verbose)
    if result != "SAT":
        if verbose:
            print("The given board is not solvable")
        return None
    solution = compute_solution(sat_assignment, variables, size)
    if verbose:
        print_solution(solution)
    return sat_assignment


class Board(object):
    """ A Sudoku board of size 9x9, possibly with some pre-filled values. """
    def __init__(self, string):
        """ Create a Board object from a single-string representation with 81 chars in the .[1-9]
         range, where a char '.' means that the position is empty, and a digit in [1-9] means that
         the position is pre-filled with that value. """
        size = math.sqrt(len(string))
        if not size.is_integer():
            raise RuntimeError(f'The specified board has length {len(string)} and does not seem to be square')
        self.data = [0 if x == '.' else int(x) for x in string]
        self.size_ = int(size)

    def size(self):
        """ Return the size of the board, e.g. 9 if the board is a 9x9 board. """
        return self.size_

    def value(self, x, y):
        """ Return the number at row x and column y, or a zero if no number is initially assigned to
         that position. """
        return self.data[x*self.size_ + y]

    def all_coordinates(self):
        """ Return all possible coordinates in the board. """
        return ((x, y) for x, y in itertools.product(range(self.size_), repeat=2))

    def print(self):
        """ Print the board in "matrix" form. """
        assert self.size_ == 9
        for i in range(self.size_):
            base = i * self.size_
            row = self.data[base:base + 3] + ['|'] + self.data[base + 3:base + 6] + ['|'] + self.data[base + 6:base + 9]
            print(" ".join(map(str, row)))
            if (i + 1) % 3 == 0:
                print("")  # Just an empty line


def main(argv):
    args = parse_arguments(argv)
    board = Board(args.board)

    if args.count:
        count_number_solutions(board, verbose=False)
    else:
        find_one_solution(board, verbose=not args.quiet)


if __name__ == "__main__":
    main(sys.argv[1:])
