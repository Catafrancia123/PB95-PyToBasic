from itertools import chain

# ill add more later - catamapp
SUPPORTED_FUNCTIONS_OLD = [
    'print', 'input', 'color',
    'fill', 'cls', 'sin', 'beep',
    'cos', 'tan', 'rnd', 'background',
    'plot', 'line', 'circle'
]

SUPPORTED_FUNCTIONS_NO_ARGS = {
    "clear" : "CLS",
}
SUPPORTED_FUNCTIONS_ONE_ARGS = {
    "print" : "PRINT",
    "print_var" : "PRINT",
    "random" : "RND",
}
SUPPORTED_FUNCTIONS_MULTIPLE_ARGS = {
    "variable" : "LET",
}

INSTRUCTIONS = {}

def translate(line_number : int, function : str, value = None):
    function = function.lower()
    if function not in chain(SUPPORTED_FUNCTIONS_NO_ARGS, SUPPORTED_FUNCTIONS_ONE_ARGS, SUPPORTED_FUNCTIONS_MULTIPLE_ARGS):
        raise NotImplementedError("Function not implemented yet, please come back later.")
    
    if type(value) == str and function != "print_var":
        value = f"\"{value.upper()}\""
    elif type(value) == str and function == "print_var":
        value = value.upper()

    if function in SUPPORTED_FUNCTIONS_MULTIPLE_ARGS:
        INSTRUCTIONS[line_number] = SUPPORTED_FUNCTIONS_MULTIPLE_ARGS[function], value
        line_number += 1
    elif function in SUPPORTED_FUNCTIONS_ONE_ARGS:
        INSTRUCTIONS[line_number] = SUPPORTED_FUNCTIONS_ONE_ARGS[function], value
        line_number += 1
    elif function in SUPPORTED_FUNCTIONS_NO_ARGS:
        INSTRUCTIONS[line_number] = SUPPORTED_FUNCTIONS_NO_ARGS[function]
        line_number += 1

    with open("output.txt", "w") as file:
        for line, command in INSTRUCTIONS.items():
            # special commands
            if isinstance(command, tuple) and command[0] == "LET":
                _, (var_name, var_value) = command  # unpack #2
                file.write(f"{line:02d} LET {var_name.upper()} = {var_value}\n")
                continue

            # basic handling
            if isinstance(command, tuple):  # one args
                l_command, l_value = command
                file.write(f"{line:02d} {l_command} {l_value}\n")
            else:  # no args
                file.write(f"{line:02d} {command}\n")
        file.close()