"""_summary_

Returns:
    _type_: _description_
"""

import re
import dicts as d

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

def is_valid_variable_name(name):
    """Check if a variable name is valid."""
    # Check if the second character is not a digit
    if name[1].isdigit():
        return False
    # Check if the name contains only allowed characters after the first character
    if not re.match(r'^[a-zA-Z0-9_$:.]*$', name[1:]):
        return False
    return True


def split_line(line):
    """Split line into components."""
    dest = "null"  # Initialize dest with a default value
    jump = "null"  # Initialize jump with a default value
    
    if "=" in line:
        dest, comp_and_jump = line.split("=")
    else:
        comp_and_jump = line  # If "=" is not present, the whole line is computation and jump
    
    if ";" in comp_and_jump:
        comp, jump = comp_and_jump.split(";")
    else:
        comp = comp_and_jump  # If ";" is not present, the whole comp_and_jump is computation
    
    return comp, dest, jump

def find_key(key, search_dict):
    """Search for dest in symbol_dict and return its value."""
    if key in search_dict:
        return search_dict[key]
    else:
        return None

def first_pass(parsed_list:list):
    """_summary_

    Args:
        parsed_list (list): _description_

    Returns:
        _type_: _description_
    """
    line_count = 0
    symbol_dict = d.init_symbol_table_dict()

    for line in parsed_list:
        if line.startswith("("):
            label = line.replace("(", "").replace(")", "")
            symbol_dict[label] = format(line_count, '015b')
        else:
            line_count += 1
    
    parsed_list = [line for line in parsed_list if not line.startswith('(')]


    return parsed_list, symbol_dict


def second_pass(parsed_list, binary_list, symbol_dict):
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
                symbol_value = "0"
                if after_at in symbol_dict:
                    symbol_value += find_key(after_at, symbol_dict)
                    binary_list.append(symbol_value)
                else:
                    binary_value = format(var_count, '016b')  # Ensure 16 bits

                    symbol_value += binary_value[-15:]  # Take only the last 15 bits
                    symbol_dict[after_at] = symbol_value
                    binary_list.append(symbol_dict[after_at])
                    var_count += 1
        else:
            binary_list = c_instruct(line, binary_list)


    return binary_list



def generate_machine_code(parsed_list, binary_list) -> str:
    """ 

    Args:
        line (str): _description_

    Returns:
        str: _description_
    """

    parsed_list, symbol_dict = first_pass(parsed_list)
    binary_list = second_pass(parsed_list, binary_list, symbol_dict)

    return binary_list

def a_instruct(line, binary_list):
    line = line[1:]
    num = int(line)
    binary_num = '0'
    binary = format(num, '015b')
    binary = str(binary)
    binary_num += binary

    binary_list.append(binary_num)

    return binary_list


def c_instruct(line, binary_list) -> list:
    #turn this into the C_instruction function
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

def l_instruct():
    pass

def write_to_hack_file(binary_list, input_filename):
    output_filename = input_filename.rsplit('.', 1)[0] + '_aspen.hack'
    with open(output_filename, 'w', encoding="utf-8") as hack_file:
        for binary_line in binary_list:
            hack_file.write(binary_line + '\n')

def ensure_16_bits(binary_list):
    for i in range(len(binary_list)):
        if len(binary_list[i]) > 16:
            binary_list[i] = binary_list[i][1:]
    return binary_list
