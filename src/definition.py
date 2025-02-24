from src.translator import translate

class Commands:
    def __init__(self):
        self.line_number : int = 1

    def print(self, value):
        """Default print command found in every programming language."""
        translate(self.line_number, "print", value)
        self.line_number += 1
        