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

    # first pass() ?
    line_count = 0
    var_count = 0
    VAR_REGISTER = 16
    symbol_dict = init_symbol_table_dict()

    for line_count, line in enumerate(parsed_lines):
        # try and except here?
        if "(" in line:
            label = line
            symbol_dict[label] = line_count + 1
        elif line.startswith("@") and line[1].isalpha():
            symbol_dict[line] = VAR_REGISTER + var_count
            var_count += 1
    parsed_lines = [line for line in parsed_lines if not line.startswith('(')]

    print(parsed_lines)
    print(symbol_dict)

    # generate machine code
    # Second pass()?
    for line in parsed_lines:
        


    # write machine code to a file

def init_symbol_table_dict() -> dict:
    """_summary_

    Args:
        key_var (_type_): _description_

    Returns:
        dict: _description_
    """
    symbol_lookup = {}

    return symbol_lookup




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

    return comp_lookup

def init_dest_lookup_dict() -> dict:
    """_summary_

    Returns:
        dict: _description_
    """
    # build dest look up dict as a comp instruction as the key and its control bits as the value
    dest_lookup = {}

    dest_lookup["null"]    = "000"
    dest_lookup["M"]   = "001"
    dest_lookup["D"]   = "010"
    dest_lookup["DM"]  = "011"
    dest_lookup["A"]   = "100"
    dest_lookup["AM"]  = "101"
    dest_lookup["AD"]  = "110"
    dest_lookup["ADM"] = "111"

    return dest_lookup

def init_jump_lookup_dict() -> dict:
    """_summary_

    Returns:
        dict: _description_
    """
    # build jump look up dict as a comp instruction as the key and its control bits as the value
    jump_lookup = {}

    jump_lookup["null"] = "000"
    jump_lookup["JGT"]  = "001"
    jump_lookup["JEQ"]  = "010"
    jump_lookup["JGE"]  = "011"
    jump_lookup["JLT"]  = "100"
    jump_lookup["JNE"]  = "101"
    jump_lookup["JLE"]  = "110"
    jump_lookup["JMP"]  = "111"

    return jump_lookup

def generate_machine_code(line: str) -> str:
    """ 

    Args:
        line (str): _description_

    Returns:
        str: _description_
    """
    #take line, check for A_instruction, C_instruction, or L_instruction, break line into components
    # as needed, interact with symbol table as needed
    # use lookup dictionaries to translate asm to hack and return hack
    pass







if __name__ == "__main__":
    main()
