#!/usr/bin/env python3

import argparse
import sys
import os


def parse_arguments(argv):
    parser = argparse.ArgumentParser(description='Solve Sudoku problems.')
    parser.add_argument("-i", help="Path to the file with the Sokoban instance.")
    return parser.parse_args(argv)


class SokobanGame(object):
    """ A Sokoban Game. """
    def __init__(self, string):
        """ Create a Sokoban game object from a string representation such as the one defined in
            http://sokobano.de/wiki/index.php?title=Level_format
        """
        lines = string.split('\n')
        self.h, self.w = len(lines), max(len(x) for x in lines)
        self.player = None
        self.walls = set()
        self.boxes = set()
        self.goals = set()
        for i, line in enumerate(lines, 0):
            for j, char in enumerate(line, 0):
                if char == '#':  # Wall
                    self.walls.add((i, j))
                elif char == '@':  # Player
                    assert self.player is None
                    self.player = (i, j)
                elif char == '+':  # Player on goal square
                    assert self.player is None
                    self.player = (i, j)
                    self.goals.add((i, j))
                elif char == '$':  # Box
                    self.boxes.add((i, j))
                elif char == '*':  # Box on goal square
                    self.boxes.add((i, j))
                    self.goals.add((i, j))
                elif char == '.':  # Goal square
                    self.goals.add((i, j))
                elif char == ' ':  # Space
                    pass  # No need to do anything
                else:
                    raise ValueError(f'Unknown character "{char}"')

    def is_wall(self, x, y):
        """ Whether the given coordinate is a wall. """
        return (x, y) in self.walls

    def is_box(self, x, y):
        """ Whether the given coordinate has a box. """
        return (x, y) in self.boxes

    def is_goal(self, x, y):
        """ Whether the given coordinate is a goal location. """
        return (x, y) in self.goals


def main(argv):
    args = parse_arguments(argv)
    with open(args.i, 'r') as file:
        board = SokobanGame(file.read().rstrip('\n'))
    num_variables = max(board.h, board.w)
    objects_line = '(:objects'
    init_line = '(:init '
    for var in range(num_variables):
        objects_line += ' v'+str(var)+''
        for var2 in range(num_variables):
            if var+1==var2:
                init_line += '(inc v'+str(var)+' v'+str(var2)+') '
                init_line += '(dec v'+str(var2)+' v'+str(var)+') '
                init_line += '\n'
    init_line += '(at player v'+str(board.player[0])+' v'+str(board.player[1])+')'
    init_line += '\n'
    for box in board.boxes:
        init_line += '(at box v'+str(box[0])+' v'+str(box[1])+') '
        init_line += '\n'
    for wall in board.walls:
        init_line += '(at wall v'+str(wall[0])+' v'+str(wall[1])+') '
        init_line += '\n'
    goal_line = '(:goal (and '
    for goal in board.goals:
        goal_line += '(at box v'+str(goal[0])+' v'+str(goal[1])+') '
        goal_line += '\n'
    lines = ['(define (problem sokobanlevel)'+'\n'+'(:domain sokoban)', objects_line+')', init_line+')', goal_line+')))']
    with open("instance.pddl", 'w') as instance:
        for line in lines:
            instance.write(line)
            instance.write('\n')

    #domain_file = open('domain.pddl', 'r')
    #instance_file = open('instance.pddl', 'r')
    #result_file = os.popen('python3 ./downward/fast-downward.py domain.pddl instance.pddl --search "astar(lmcut())"')
    result_file = os.popen('python3 ./downward/fast-downward.py --alias seq-sat-lama-2011 domain.pddl instance.pddl')
    result = result_file.readlines()
    actions = []
    for line in result:
        if ('push' in line) or ('move' in line) or ('teleport' in line): 
            print(line)
            actions.append(line)

    # TODO - Some of the things that you need to do:
    #  1. (Previously) Have a domain.pddl file somewhere in disk that represents the Sokoban actions and predicates. done
    #  2. Generate an instance.pddl file from the given board, and save it to disk. done
    #  3. Invoke some classical planner to solve the generated instance.
    #  4. Check the output and print the plan into the screen in some readable form.
    


if __name__ == "__main__":
    main(sys.argv[1:])
