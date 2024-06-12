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
    components = line.split('=')
    dest = components[0] if components[0] else "null"  # Save the destination (before "="), or "null" if empty
    if len(components) == 2:  # If "=" is present
        components = components[1].split(';')  # Split the part after "=" by ";"
        comp = components[0]  # Save the computation part (between "=" and ";")
        jump = components[1] if len(components) > 1 and components[1] else "null"  # Save the jump part (after ";"), or "null" if empty
    else:  # If "=" is not present
        comp = components[0]  # Save the computation part as the whole line
        jump = "null"  # No jump part, so return "null"
    return comp, dest, jump

def find_key(key, dict):
    """Search for dest in symbol_dict and return its value."""
    if key in dict:
        return dict[key]
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
    var_count = 0
    VAR_REGISTER = 16
    symbol_dict = d.init_symbol_table_dict()

    for line_count, line in enumerate(parsed_list):
        if line.startswith("("):
            label = line
            symbol_dict[label] = line_count + 1
        elif line.startswith("@"):
            symbol_dict[line] = VAR_REGISTER + var_count
            var_count += 1
    parsed_list = [line for line in parsed_list if not line.startswith('(')]
    print(f"Parsed lines (first)pass: {parsed_list}")

    return parsed_list, symbol_dict

def second_pass(parsed_list, binary_list, symbol_dict):
    for line in parsed_list:
        if line.startswith("@"):
            valid_var = is_valid_variable_name(line)
            at_index = line.index('@')
            after_at = line[at_index + 1:]
            # EX @12
            if all(char.isdigit() for char in line[after_at:]):
                valid_var = True
                # A_instruction
            # EX @1var
            elif not valid_var:
                raise ValueError(f"Variable {line} does not follow variable naming conventions.\n"
                                 "Please review input file. Variables should contain letters or "
                                 "letters and numbers, but should not begin with a number.\n")
            else:
            # EX @var or @var1
                if after_at.isalnum():
                    if after_at in symbol_dict:
                        pass
                        # A-instrct
                    else:
                        pass
                        # add to symbol table
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
    #take line, check for A_instruction, C_instruction, or L_instruction, break line into components
    # as needed, interact with symbol table as needed
    # use lookup dictionaries to translate asm to hack and return hack
    parsed_list, symbol_dict = first_pass(parsed_list)
    binary_list = second_pass(parsed_list, binary_list, symbol_dict)

    return binary_list

def a_instruct():
    pass

def c_instruct(line, binary_list) -> list:
    #turn this into the C_instruction function
    binary_line = "111"
    comp, dest, jump = split_line(line)

    comp_dict = d.init_comp_lookup_dict()
    dest_dict = d.init_dest_lookup_dict()
    jump_dict = d.init_jump_lookup_dict()

    comp_value = find_key(comp, comp_dict)
    if comp_value is None:
        raise KeyError(f"Key {comp_value} not found in {comp_dict}.")
    binary_line += comp_value

    dest_value = find_key(dest, dest_dict)
    if dest_value is None:
        raise KeyError(f"Key {dest_value} not found in {dest_dict}.")
    binary_line += dest_value

    jump_value = find_key(jump, jump_dict)
    if jump_value is None:
        raise KeyError(f"Key {jump_value} not found in {jump_dict}.")
    binary_line += jump_value
    binary_list.append(binary_line)

    return binary_list

def l_instruct():
    pass
