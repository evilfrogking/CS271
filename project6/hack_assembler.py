"""
File: hack_assembler.py
Author: Aspen Frazee
Date: 6/12/2024
Summary: Program input an assembly program and converts it into a hack program
to be run on the Nand2Tetris CPU simulator.
"""

import sys
import functions as f


def main():
    """Opens a file, runs the necessary computations,
    and write the results to a hack file.
    """
    input_filename = sys.argv[1]
    input_file_contents = []

    with open(input_filename, "r", encoding="utf-8") as input_file:
        input_file_contents = input_file.readlines()

    parsed_lines = []
    for line in input_file_contents:
        parsed_line = f.parse(line)
        if parsed_line != "":
            parsed_lines.append(parsed_line)

    binary_lines = []
    binary_lines = f.generate_machine_code(parsed_lines, binary_lines)

    f.write_to_hack_file(binary_lines, input_filename)


if __name__ == "__main__":
    main()
