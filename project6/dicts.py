"""_summary_
"""

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
    dest_lookup["MD"]  = "011"
    
    dest_lookup["A"]   = "100"

    dest_lookup["AM"]  = "101"
    dest_lookup["MA"]  = "101"

    dest_lookup["AD"]  = "110"
    dest_lookup["DA"]  = "110"

    dest_lookup["ADM"] = "111"
    dest_lookup["AMD"] = "111"
    dest_lookup["DAM"] = "111"
    dest_lookup["DMA"] = "111"
    dest_lookup["MAD"] = "111"
    dest_lookup["MDA"] = "111"

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

def init_symbol_table_dict() -> dict:
    """_summary_

    Args:
        key_var (_type_): _description_

    Returns:
        dict: _description_
    """
    symbol_lookup = {}

    symbol_lookup['SP']     = "000000000000000"
    symbol_lookup['LCL']    = "000000000000001"
    symbol_lookup['ARG']    = "000000000000010"
    symbol_lookup['THIS']   = "000000000000011"
    symbol_lookup['THAT']   = "000000000000100"
    symbol_lookup['R0']     = "000000000000000"
    symbol_lookup['R1']     = "000000000000001"
    symbol_lookup['R2']     = "000000000000010"
    symbol_lookup['R3']     = "000000000000011"
    symbol_lookup['R4']     = "000000000000100"
    symbol_lookup['R5']     = "000000000000101"
    symbol_lookup['R6']     = "000000000000110"
    symbol_lookup['R7']     = "000000000000111"
    symbol_lookup['R8']     = "000000000001000"
    symbol_lookup['R9']     = "000000000001001"
    symbol_lookup['R10']    = "000000000001010"
    symbol_lookup['R11']    = "000000000001011"
    symbol_lookup['R12']    = "000000000001100"
    symbol_lookup['R13']    = "000000000001101"
    symbol_lookup['R14']    = "000000000001110"
    symbol_lookup['R15']    = "000000000001111"
    symbol_lookup['SCREEN'] = "100000000000000"
    symbol_lookup['KBD']    = "110000000000000"

    return symbol_lookup

