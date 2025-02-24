from src.translator import translate

class Commands:
    def __init__(self):
        self.line_number : int = 1

    def __str__(self) -> str:
        return "dear user, please for the love of god dont print the class!!!"

    def print(self, value, var = False):
        """Displays text on the output, found in every programming language."""
        if var == True:
            translate(self.line_number, "print_var", value)
        else:
            translate(self.line_number, "print", value)
        self.line_number += 1

    def clear(self):
        """Clears the screen. (do we even need this?? its a basic CLS!!!)"""
        translate(self.line_number, "clear")
        self.line_number += 1
    
    def random(self, end : int):
        """Generates a random number from 1 to x. (x = end number)"""
        translate(self.line_number, "random", end)
        self.line_number += 1

    def let(self, var_name : str, value):
        """Makes a variable."""
        value_list = (var_name, value)
        translate(self.line_number, "variable", value_list)
        self.line_number += 1
        