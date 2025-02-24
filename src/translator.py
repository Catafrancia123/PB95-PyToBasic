# ill add more later - catamapp
SUPPORTED_FUNCTIONS_OLD = [
    'print', 'input', 'color',
    'fill', 'cls', 'sin', 'beep',
    'cos', 'tan', 'rnd', 'background',
    'plot', 'line', 'circle'
]

SUPPORTED_FUNCTIONS_ONE_ARGS = {
    "print" : "PRINT",
}

INSTRUCTIONS = {}

def translate(line_number : int, function : str, value = None):
    function.lower()
    if function not in SUPPORTED_FUNCTIONS_ONE_ARGS:
        raise NotImplementedError("Function not implemented yet, please come back later.")
    if type(value) == str:
        value.upper()
        value = f"\"{value}\""
    
    if function in SUPPORTED_FUNCTIONS_ONE_ARGS:
        INSTRUCTIONS[line_number] = SUPPORTED_FUNCTIONS_ONE_ARGS[function], value
        line_number += 1

    with open("output.txt", "w") as file:
        try:
            for line, (command, l_value) in INSTRUCTIONS.items():
                file.write(f"{line:02d} {command} {l_value}\n")
        except ValueError:
            for line, (command) in INSTRUCTIONS.items():
                file.write(f"{line:02d} {command}\n")
