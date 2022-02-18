import sys

EMPTY_SUDOKU = [0]
DIMACS_CNF_FILE = "res/dimacs.cnf"

D = 3    # Subgrid dimension
N = D*D  # Grid dimension

class HelperCNF():

    def __init__(self):
        print("DIMACS CNF FORMAT")

    def sat_encoder(self, input_sudoku, cnf_path):
        print("Input is :\n", input_sudoku)

    def sat_decoder(self):
        print("Output is: \n")


if __name__ == '__main__':
    cnf_handler = HelperCNF()
