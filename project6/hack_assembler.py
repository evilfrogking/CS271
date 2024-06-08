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

def init_comp_lookup_dict() -> dict:
    """_summary_

    Returns:
        dict: _description_
    """
    # build comp look up dict as a comp instruction as the key and its control bits as the value
    comp_lookup = {}
    #A'S
    comp_lookup["0"]   = "0101010"
    comp_lookup["1"]   = "0111111"
    comp_lookup["-1"]  = "0111010"
    comp_lookup["D"]   = "0001100"
    comp_lookup["A"]   = "0110000"
    comp_lookup["!D"]  = "0001101"
    comp_lookup["!A"]  = "0110001"
    comp_lookup["-D"]  = "0001111"
    comp_lookup["-A"]  = "0110011"
    comp_lookup["D+1"] = "0011111"
    comp_lookup["A+1"] = "0110111"
    comp_lookup["D-1"] = "0001110"
    comp_lookup["A-1"] = "0110010"
    comp_lookup["D+A"] = "0000010"
    comp_lookup["D-A"] = "0010011"
    comp_lookup["A-D"] = "0000111"
    comp_lookup["D&A"] = "0000000"
    comp_lookup["D|A"] = "0010101"
    # M'S
    comp_lookup["M"]   = "1110000"
    comp_lookup["!M"]  = "1110001"
    comp_lookup["-M"]  = "1110011"
    comp_lookup["M+1"] = "1110111"
    comp_lookup["M-1"] = "1110010"
    comp_lookup["D+M"] = "1000010"
    comp_lookup["D-M"] = "1010011"
    comp_lookup["M-D"] = "1000111"
    comp_lookup["D&M"] = "1000000"
    comp_lookup["D|M"] = "1010101"





if __name__ == "__main__":
    main()
