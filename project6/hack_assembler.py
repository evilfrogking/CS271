''' Class code'''
import sys


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
        parsed_line = parse(line)
        if parsed_line != "":
            parsed_lines.append(parsed_line)

    print(f"parsed_lines: {parsed_lines}")

    # generate machine code

    # write machine code to a file


def parse(input_line: str) -> str:
    """_summary_

    Args:
        input_line (str): _description_

    Returns:
        str: _description_
    """
    # strip whitespace
    output_line = input_line.strip()

    # double forward slash detector with split
    # makes the line a list, assigns the first elem to the variable, disposes of the rest
    output_line = output_line.split('//')[0]
    # removes any whitespace in a line
    for char in output_line:
        if char == " ":
            output_line = output_line.replace(" ", "")

    return output_line


if __name__ == "__main__":
    main()
