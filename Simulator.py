to_open="test.txt"
to_write = "simulator.txt"

line_list = []
main_list = []
r_type_opcode = ["0110011"]
i_type_opcode = ["0000011", "0010011", "1100111"]
s_type_opcode = ["0100011"]
b_type_opcode = ["1100011"]
u_type_opcode = ["0110111", "0010111"]
j_type_opcode = ["1101111"]

registers_list = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19", "x20", "x21", "x22", "x23", "x24", "x25", "x26", "x27", "x28", "x29", "x30", "x31"]

memory_values = {
    "00010000": 0,
    "00010004": 0,
    "00010008": 0,
    "0001000c": 0,
    "00010010": 0,
    "00010014": 0,
    "00010018": 0,
    "0001001c": 0,
    "00010020": 0,
    "00010024": 0,
    "00010028": 0,
    "0001002c": 0,
    "00010030": 0,
    "00010034": 0,
    "00010038": 0,
    "0001003c": 0,
    "00010040": 0,
    "00010044": 0,
    "00010048": 0,
    "0001004c": 0,
    "00010050": 0,
    "00010054": 0,
    "00010058": 0,
    "0001005c": 0,
    "00010060": 0,
    "00010064": 0,
    "00010068": 0,
    "0001006c": 0,
    "00010070": 0,
    "00010074": 0,
    "00010078": 0,
}

register_values = {
    "x0": 0,
    "x1": 0,
    "x2": 0,
    "x3": 0,
    "x4": 0,
    "x5": 0,
    "x6": 0,
    "x7": 0,
    "x8": 0,
    "x9": 0,
    "x10": 0,
    "x11": 0,
    "x12": 0,
    "x13": 0,
    "x14": 0,
    "x15": 0,
    "x16": 0,
    "x17": 0,
    "x18": 0,
    "x19": 0,
    "x20": 0,
    "x21": 0,
    "x22": 0,
    "x23": 0,
    "x24": 0,
    "x25": 0,
    "x26": 0,
    "x27": 0,
    "x28": 0,
    "x29": 0,
    "x30": 0,
    "x31": 0
}

register_decoder = {
    "00000": "x0",
    "00001": "x1",
    "00010": "x2",
    "00011": "x3",
    "00100": "x4",
    "00101": "x5",
    "00110": "x6",
    "00111": "x7",
    "01000": "x8",
    "01001": "x9",
    "01010": "x10",
    "01011": "x11",
    "01100": "x12",
    "01101": "x13",
    "01110": "x14",
    "01111": "x15",
    "10000": "x16",
    "10001": "x17",
    "10010": "x18",
    "10011": "x19",
    "10100": "x20",
    "10101": "x21",
    "10110": "x22",
    "10111": "x23",
    "11000": "x24",
    "11001": "x25",
    "11010": "x26",
    "11011": "x27",
    "11100": "x28",
    "11101": "x29",
    "11110": "x30",
    "11111": "x31"
}

binary_to_hex = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}

# def decimal_to_binary(imm, max_bits, signed = True):
#     if imm < (-(2*(max_bits-1))) or imm > ((2*(max_bits-1))-1):
#         return False
#     else:
#         binary = ""
#         if(imm>=0):
#             while imm > 0:
#                 rem = str(imm % 2)
#                 binary = rem + binary
#                 imm //= 2
#         else:
#             temp = abs(int(pow(2,max_bits)-1) - abs(imm) + 1)
#             while temp > 0:
#                 rem = str(temp % 2)
#                 binary = rem + binary
#                 temp //= 2

#         if len(binary) < max_bits:
#             if(signed == True):
#                 if imm < 0:
#                     binary = "1" * (max_bits - len(binary)) + binary
#                 else:
#                     binary = "0" * (max_bits - len(binary)) + binary
#             else:
#                 binary = "0" * (max_bits - len(binary)) + binary
#         return binary

# def binary_sign_extension(binary, max_bits, signed = True):
#     no_of_bits = len(binary)
#     bit_to_extend = max_bits - no_of_bits
#     if(signed == True):
#         if(binary[0] == "0"):
#             binary = "0"*bit_to_extend + binary
#         elif(binary[0] == "1"):
#             binary = "1"*bit_to_extend + binary
#     else:
#         binary = "0"*bit_to_extend + binary
#     return binary

# def binary_to_decimal(binary):
#     converted = 0
#     no_of_bits = len(binary)
#     converted = converted + (int(binary[0]))(-1(int(binary[0])))(2**(no_of_bits-1))
#     for i in range(1,no_of_bits):
#         converted = converted + (int(binary[i]))(2*(no_of_bits-i-1))
#     return converted

def decimal_to_binary(imm):
    binary = ""
    if(imm>=0):
        while imm > 0:
            rem = str(imm % 2)
            binary = rem + binary
            imm //= 2
        binary = "0" + binary
    else:
        temp = abs(imm)
        while temp > 0:
            rem = str(temp % 2)
            binary = rem + binary
            temp //= 2
        binary = "0"+binary
        flipped_binary = ""
        for i in range(0, len(binary)):
            flipped_binary = flipped_binary + str(1-int(binary[i]))
        binary = flipped_binary
        binary = str(int(binary) + 1)
    return binary

def binary_sign_extension(binary, max_bits, signed = True):
    no_of_bits = len(binary)
    bit_to_extend = max_bits - no_of_bits
    if(signed == True):
        if(binary[0] == "0"):
            binary = "0"*bit_to_extend + binary
        elif(binary[0] == "1"):
            binary = "1"*bit_to_extend + binary
    else:
        binary = "0"*bit_to_extend + binary
    return binary

def binary_to_decimal(binary, signed = True):
    converted = 0
    if(signed == True):
        no_of_bits = len(binary)
        converted = converted + (int(binary[0]))(-1(int(binary[0])))(2**(no_of_bits-1))
        for i in range(1,no_of_bits):
            converted = converted + (int(binary[i]))(2*(no_of_bits-i-1))
    else:
        no_of_bits = len(binary)
        for i in range(0,no_of_bits):
            converted = converted + (int(binary[i]))(2*(no_of_bits-i-1))
    return converted

def binary_to_hexadecimal(binary_str):
    hexadecimal_string = ""
    for i in range(0, len(binary_str), 4):
        hexadecimal_string += binary_to_hex[binary_str[i:i+4]]
    return hexadecimal_string

def r_type_instruction(line):
    pass

def i_type_instruction(line, line_number):
    line_number_to_return = line_number
    temp_list = []
    opcode = line[25:32]
    destination_register = line[20:25]
    func3 = line[17:20]
    source_register = line[12:17]
    immediate = line[0:12]
    destination_register = register_decoder[destination_register]
    source_register = register_decoder[source_register]
    if(opcode == "0000011" and func3 == "010"):
        source_register = register_values[source_register]
        immediate = binary_to_decimal(binary_sign_extension(immediate, 32))
        memory = binary_to_hexadecimal(decimal_to_binary(source_register + immediate))
        register_values[destination_register] = memory_values[memory]

    elif(opcode == "0010011" and func3 == "000"):
        immediate = binary_to_decimal(immediate)
        register_values[destination_register] = register_values[source_register] + immediate

    elif(opcode == "0010011" and func3 == "011"):
        unsinged_rs = binary_sign_extension(decimal_to_binary(register_values[source_register]), 32, False)
        unsigned_imm = binary_sign_extension(immediate, 32, False)
        unsinged_rs = binary_to_decimal(unsinged_rs, False)
        unsigned_imm = binary_to_decimal(unsigned_imm, False)
        if(unsinged_rs<unsigned_imm):
            register_values[destination_register] = 1

    elif(opcode == "1100111" and func3=="000"): #jalr incomplete
        register_values[destination_register] = (line_number*4)+4
        immediate = binary_to_decimal(binary_sign_extension(immediate, 32))
        program_counter = register_values["x6"] + immediate
        program_counter = decimal_to_binary(program_counter)
        program_counter = program_counter[0:31] + "0"
        to_append = "0b" + program_counter
        temp_list.append(to_append)
        program_counter = binary_to_decimal(program_counter, False)
        line_number_to_return = program_counter/4
        line_number_to_return-=1
        for i in range(32):
            value_is = "0b" + binary_sign_extension(decimal_to_binary(register_values[registers_list[i]]), 32)
            temp_list.append(value_is)
        main_list.append(temp_list)
        return line_number_to_return

    line_number = line_number*4
    line_number = "0b" + binary_sign_extension(decimal_to_binary(line_number), 32)
    temp_list.append(line_number)
    for i in range(32):
        value_is = "0b" + binary_sign_extension(decimal_to_binary(register_values[registers_list[i]]), 32)
        temp_list.append(value_is)
    main_list.append(temp_list)
    return line_number_to_return


def s_type_instruction(line):
    pass

def b_type_instruction(line, line_number):
    return line_number

def u_type_instruction(line, line_number):
    temp_list = []
    Program_counter = line_number*4
    opcode = line[25:32]
    destination_register = line[20:25]
    immediate = line[0:20]
    if(opcode == "0010111"):
        register_values[register_decoder[destination_register]] = Program_counter + binary_to_decimal(binary_sign_extension((immediate + 12*"0"), 32, False))
    elif (opcode == "0110111"):
        register_values[register_decoder[destination_register]] = binary_to_decimal(binary_sign_extension((immediate + 12*"0"), 32, False))
    line_number = line_number*4
    line_number = "0b" + binary_sign_extension(decimal_to_binary(line_number), 32)
    temp_list.append(line_number)
    for i in range(32):
        value_is = "0b" + binary_sign_extension(decimal_to_binary(register_values[registers_list[i]]), 32)
        temp_list.append(value_is)
    main_list.append(temp_list)


def j_type_instruction(line):
    pass

with open(to_open) as f:
    for line in f:    
        curr_line = line.strip()
        line_list.append(curr_line)


line_number = 0
while(line_number<len(line_list)):
    line = line_list[line_number];   
    curr_line = line.strip()
    instruction_opcode = curr_line[25:31]   
    if(instruction_opcode in r_type_opcode):
        r_type_instruction(curr_line)   
            
    elif(instruction_opcode in i_type_opcode):
        line_number = i_type_instruction(curr_line, line_number)
        
    elif(instruction_opcode in s_type_opcode):
        s_type_instruction(curr_line)

    elif(instruction_opcode in b_type_opcode):
        line_number = b_type_instruction(curr_line, line_number)

    elif(instruction_opcode in u_type_opcode):
        u_type_instruction(curr_line, line_number)

    elif(instruction_opcode in j_type_opcode):
        j_type_instruction(curr_line)

    line_number+=1