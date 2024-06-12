"""
File: functions.py
Author: Aspen Frazee
Date: 6/12/2024
Summary: File for functions used in the hack_assembler.py
"""

import re
import dicts as d


def parse(input_line: str) -> str:
    """Chews up the input lines and spits out pretty chunks for the assembler.

    Args:
        input_line (str): A line from the input file.

    Returns:
        str: A cleaned up line to become an element in the parsed_lines list.
    """
    output_line = input_line.strip()

    # makes the line a list, assigns the first elem to the variable, disposes of the rest
    output_line = output_line.split('//')[0]

    for char in output_line:
        if char == " ":
            output_line = output_line.replace(" ", "")

    return output_line


def is_valid_variable_name(name):
    """Check if a variable name is valid.

    Args:
        name (variable): @variable

    Returns:
        Boolean: confirms if the variable name is valid, otherwise false.
    """
    if name[1].isdigit():
        return False
    # Check if the name contains only allowed characters after the first character
    if not re.match(r'^[a-zA-Z0-9_$:.]*$', name[1:]):
        return False
    return True


def split_line(line):
    """Split line into components; only c-instructions.

    Args:
        line (string): parsed lines to be split into it's components.

    Returns:
        str: returns the str segments of comp, dest, and jump
    """
    dest = "null"
    jump = "null"

    if "=" in line:
        dest, comp_and_jump = line.split("=")
    else:
        comp_and_jump = line

    if ";" in comp_and_jump:
        comp, jump = comp_and_jump.split(";")
    else:
        comp = comp_and_jump

    return comp, dest, jump


def find_key(key, search_dict):
    """Search for dest in symbol_dict and return its value.

    Args:
        key (str): variable to be searched for in dictionary.
        search_dict (dict): Dictionary of choice for the desired value.

    Returns:
        str: returns the corresponding binary string.
    """
    if key in search_dict:
        return search_dict[key]
    else:
        return None


def first_pass(parsed_list:list):
    """First pass counts the number of lines, builds the labels into the symbol table,
    and 

    Args:
        parsed_list (list): List of lines from the input file.

    Returns:
        parsed_list: returns a list sans labels
        symbol_dict: returns the newly build symbol table
    """
    line_count = 0
    symbol_dict = d.init_symbol_table_dict()

    for line in parsed_list:
        if line.startswith("("):
            label = line.replace("(", "").replace(")", "")
            symbol_dict[label] = format(line_count, '016b')
        else:
            line_count += 1
    parsed_list = [line for line in parsed_list if not line.startswith('(')]

    return parsed_list, symbol_dict


def second_pass(parsed_list, binary_list, symbol_dict):
    """Takes the parsed pieces and assigns them to the correct function for translation, then combines them.

    Args:
        parsed_list (list): list of  lines from the input file
        binary_list (list): list of lines for the output file
        symbol_dict (dict): symbols table

    Raises:
        ValueError: Checks for valid variables in input file.

    Returns:
        binary_list: updated list of lines for the output file
    """
    var_count = 16
    for line in parsed_list:
        if line.startswith("@"):
            valid_var = is_valid_variable_name(line)
            at_index = line.index('@')
            after_at = line[at_index + 1:]
            # EX @12
            if all(char.isdigit() for char in after_at):
                valid_var = True
                binary_list = a_instruct(line, binary_list)
            # EX @1var
            elif not valid_var:
                raise ValueError(f"Variable {line} does not follow variable naming conventions.\n"
                                 "Please review input file. Variables should contain letters or "
                                 "letters and numbers, but should not begin with a number.\n")
            else:
                if after_at in symbol_dict:
                    symbol_value = find_key(after_at, symbol_dict)
                    binary_list.append(symbol_value)
                else:
                    symbol_value = ""
                    binary_value = format(var_count, '016b') 

                    symbol_dict[after_at] = binary_value
                    binary_list.append(symbol_dict[after_at])
                    var_count += 1
        else:
            binary_list = c_instruct(line, binary_list)

    return binary_list


def generate_machine_code(parsed_list, binary_list) -> str:
    """ Combines first and second pass for main file clarity.

    Args:
        parsed_list (list): list of  lines from the input file
        binary_list (list): list of lines for the output file

    Returns:
        binary_list: updated list of lines for the output file
    """

    parsed_list, symbol_dict = first_pass(parsed_list)
    binary_list = second_pass(parsed_list, binary_list, symbol_dict)

    return binary_list


def a_instruct(line, binary_list):
    """Instructions for numerical registers.

    Args:
        line (str): section of a line from the source file
        binary_list (list): list of lines for the output file

    Returns:
        _binary_list: updated list of lines for the output file
    """
    line = line[1:]
    num = int(line)
    binary_num = '0'
    binary = format(num, '015b')
    binary = str(binary)
    binary_num += binary

    binary_list.append(binary_num)

    return binary_list


def c_instruct(line, binary_list) -> list:
    """_summary_

    Args:
        line (str): section of a line from the source file
        binary_list (list): list of lines for the output file

    Raises:
        KeyError: key not found in comp dictionary
        KeyError: key not found in dest dictionary
        KeyError: key not found in jump dictionary

    Returns:
        binary_list: updated list of lines for the output file
    """
    binary_line = "111"
    comp, dest, jump = split_line(line)

    comp_dict = d.init_comp_lookup_dict()
    dest_dict = d.init_dest_lookup_dict()
    jump_dict = d.init_jump_lookup_dict()

    comp_value = find_key(comp, comp_dict)
    if comp_value is None:
        raise KeyError(f"Key {comp} not found in {comp_dict}.")
    binary_line += comp_value

    dest_value = find_key(dest, dest_dict)
    if dest_value is None:
        raise KeyError(f"Key {dest} not found in {dest_dict}.")
    binary_line += dest_value

    jump_value = find_key(jump, jump_dict)
    if jump_value is None:
        raise KeyError(f"Key {jump} not found in {jump_dict}.")
    binary_line += jump_value
    binary_list.append(binary_line)

    return binary_list


def write_to_hack_file(binary_list, input_filename):
    """Outputs the binary list to a .hack file for the CPU.
    Uses the input files name and adds my name to the end.

    Args:
        binary_list (list): list of lines for the output file
        input_filename (str): Name of the input file
    """
    output_filename = input_filename.rsplit('.', 1)[0] + '_aspen.hack'
    with open(output_filename, 'w', encoding="utf-8") as hack_file:
        for binary_line in binary_list:
            hack_file.write(binary_line + '\n')
