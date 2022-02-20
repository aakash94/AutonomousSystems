from utils import solve
from sudoku import find_one_solution, solve_sat_problem, print_solution, compute_solution

EMPTY_SUDOKU = "................................................................................."
DIMACS_Q1_FILE = "res/dimacs_q1.cnf"
DIMACS_Q2_FILE = "res/dimacs_q2.cnf"

D = 3  # Subgrid dimension
N = D * D  # Grid dimension
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def var(r, c, v):
    '''
    A helper: get the Dimacs CNF variable number for the variable v_{r,c,v}
    encoding the fact that the cell at (r,c) has the value v
    '''
    assert (1 <= r and r <= N and 1 <= c and c <= N and 1 <= v and v <= N)
    return (r - 1) * N * N + (c - 1) * N + (v - 1) + 1


def generate_q1(input_sudoku=EMPTY_SUDOKU):
    clues = [input_sudoku[i:i + N] for i in range(0, len(input_sudoku), N)]
    # print("Chunks \n", clues)
    # Build the clauses in a list
    cls = []  # The clauses: a list of integer lists
    for r in range(1, N + 1):  # r runs over 1,...,N
        for c in range(1, N + 1):
            # The cell at (r,c) has at least one value
            cls.append([var(r, c, v) for v in range(1, N + 1)])
            # The cell at (r,c) has at most one value
            for v in range(1, N + 1):
                for w in range(v + 1, N + 1):
                    cls.append([-var(r, c, v), -var(r, c, w)])
    for v in range(1, N + 1):
        # Each row has the value v
        for r in range(1, N + 1): cls.append([var(r, c, v) for c in range(1, N + 1)])
        # Each column has the value v
        for c in range(1, N + 1): cls.append([var(r, c, v) for r in range(1, N + 1)])
        # Each subgrid has the value v
        for sr in range(0, D):
            for sc in range(0, D):
                cls.append([var(sr * D + rd, sc * D + cd, v)
                            for rd in range(1, D + 1) for cd in range(1, D + 1)])
    # The clues must be respected
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if clues[r - 1][c - 1] in digits.keys():
                cls.append([var(r, c, digits[clues[r - 1][c - 1]])])

    with open(DIMACS_Q1_FILE, 'w') as cnf_file:
        line = "p cnf %d %d" % (N * N * N, len(cls))
        cnf_file.write(line)
        cnf_file.write("\n")
        for c in cls:
            line = " ".join([str(l) for l in c]) + " 0"
            cnf_file.write(line)
            cnf_file.write("\n")


def generate_q2(input_sudoku=EMPTY_SUDOKU):
    # TODO: Write Logic for this, and update DIMACS_Q2_FILE
    pass


class HelperCNF():

    def __init__(self):
        print("DIMACS CNF SAT\n\n")

    def sat_encoder(self, input_sudoku=EMPTY_SUDOKU):
        '''
        Generate a CNF File from the Input Sudoku String
        '''
        assert len(input_sudoku) == (N * N), "Wrong Sudoku Input"
        print("Input is :\n", input_sudoku)
        generate_q1(input_sudoku=input_sudoku)
        # generate_q2(input_sudoku=input_sudoku)

    def sat_decoder(self):
        print("Output is: \n")


if __name__ == '__main__':
    cnf_handler = HelperCNF()
    # Read the sudoku string from the first parameter
    # sudoku_string  = sys.argv[1]
    sudoku_string = ".......1.4.........2...........5.4.7..8...3....1.9....3..4..2...5.1........8.6..."
    cls = cnf_handler.sat_encoder(input_sudoku=sudoku_string)
    result1, sat_assignment = solve(cnf_filename=DIMACS_Q1_FILE, verbose=False)
    if result1 != "SAT":
        print("The given board is not solvable")

    solution = compute_solution(sat_assignment, size=N)
    print_solution(solution)
    # result2 = solve(cnf_filename=DIMACS_Q2_FILE)

    # TODO: Interpret and Print result1 and result2 beautifully.
