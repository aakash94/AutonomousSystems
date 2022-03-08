#!/usr/bin/env python3

import argparse
from asyncio import run_coroutine_threadsafe
import sys
import os
from translator import *

# add path to your fast-downward.py file!
downward_path = './downward/fast-downward.py'
optimal_command_solver = 'seq-opt-bjolp'
satisfiable_command_solver = 'seq-sat-lama-2011'

def parse_arguments(argv):
    parser = argparse.ArgumentParser(description='Solve Sudoku problems.')
    parser.add_argument("-i", help="Path to the file with the Sokoban instance2.")
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
    objects_line = '(:objects '
    init_line = '(:init '
    for var in range(board.h):
        for var2 in range(board.w):
            objects_line += 'v'+str(var)+'-v'+str(var2)+' '
            init_line += '(adjacent v'+str(var)+'-v'+str(var2)+' v'+str(var+1)+'-v'+str(var2)+') '
            init_line += '(adjacent v'+str(var)+'-v'+str(var2)+' v'+str(var-1)+'-v'+str(var2)+') '
            init_line += '(adjacent v'+str(var)+'-v'+str(var2)+' v'+str(var)+'-v'+str(var2+1)+') '
            init_line += '(adjacent v'+str(var)+'-v'+str(var2)+' v'+str(var)+'-v'+str(var2-1)+') '
            init_line += '(adjacent_2 v'+str(var)+'-v'+str(var2)+' v'+str(var+2)+'-v'+str(var2)+') '
            init_line += '(adjacent_2 v'+str(var)+'-v'+str(var2)+' v'+str(var-2)+'-v'+str(var2)+') '
            init_line += '(adjacent_2 v'+str(var)+'-v'+str(var2)+' v'+str(var)+'-v'+str(var2+2)+') '
            init_line += '(adjacent_2 v'+str(var)+'-v'+str(var2)+' v'+str(var)+'-v'+str(var2-2)+') '
            init_line += '\n'
        objects_line += '\n'
    init_line += '(use_teleport)'
    init_line += '\n'
    init_line += '(at player v'+str(board.player[0])+'-v'+str(board.player[1])+')'
    init_line += '\n'
    for box in board.boxes:
        init_line += '(at box v'+str(box[0])+'-v'+str(box[1])+') '
        init_line += '\n'
    for wall in board.walls:
        init_line += '(at wall v'+str(wall[0])+'-v'+str(wall[1])+') '
        init_line += '\n'
    goal_line = '(:goal (and '
    for goal in board.goals:
        goal_line += '(at box v'+str(goal[0])+'-v'+str(goal[1])+') '
        goal_line += '\n'
    lines = ['(define (problem sokobanlevel)'+'\n'+'(:domain sokoban)', objects_line+')', init_line+')', goal_line+')))']
    with open("instance.pddl", 'w') as instance:
        for line in lines:
            instance.write(line)
            instance.write('\n')

    if sys.argv[1:][1] == 'all':
        # next line to run optimal plan solver and below to run satisfiable plan solver
        #result_file = os.popen('python3 ' + downward_path + ' --overall-time-limit 60 --alias ' + optimal_command_solver + ' --plan-file myplan.txt domain.pddl instance.pddl')
        result_file = os.popen('python3 ' + downward_path + ' --overall-time-limit 60 --alias ' + satisfiable_command_solver + ' --plan-file myplan.txt domain.pddl instance.pddl')
    else:
        # Run with satisfiable plan solver due to time limitation without any time-limit
        result_file = os.popen('python3 ' + downward_path + ' --alias ' + satisfiable_command_solver + ' --plan-file myplan.txt domain.pddl instance.pddl')
    result = result_file.readlines()
    actions = []
    for line in result:
        actions.append(line)
    solution = translate()
    return solution


    # TODO - Some of the things that you need to do:
    #  1. (Previously) Have a domain.pddl file somewhere in disk that represents the Sokoban actions and predicates. done
    #actions  2. Generate an instance2.pddl file from the given board, and save it to disk. done
    #  3. Invoke some classical planner to solve the generated instance2.
    #  4. Check the output and print the plan into the screen in some readable form.


if __name__ == "__main__":
    current_level = 1
    if sys.argv[1:][1] == 'all':
        solution_dict = dict()
        while current_level <=50:
            solution = main(['-i', 'benchmarks/sasquatch/level'+str(current_level)+'.sok'])
            solution_dict[current_level] = solution
            current_level += 1
        print(solution_dict)
    else:
        main(sys.argv[1:])