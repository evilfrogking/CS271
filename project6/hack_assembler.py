''' Class code'''
import sys
import functions as f


def main():
    """_summary_
    """
    # open file
    input_filename = sys.argv[1]
    input_file_contents = []

    with open(input_filename, "r", encoding="utf-8") as input_file:
        # read into a list
        input_file_contents = input_file.readlines()

    # call parser on each line
    parsed_lines = []
    for line in input_file_contents:
        parsed_line = f.parse(line)
        if parsed_line != "":
            parsed_lines.append(parsed_line)

    binary_lines = []
    binary_lines = f.generate_machine_code(parsed_lines, binary_lines)

    f.write_to_hack_file(binary_lines, input_filename)

    # write machine code to a file


if __name__ == "__main__":
    main()
