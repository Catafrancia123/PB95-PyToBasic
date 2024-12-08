"""MIT License

Copyright (c) 2024 Bananchiki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import ast
from src.statements import assign, create_if, create_for, create_while
from src.expressions import call

def process_statement(obj, instructions_list: list[str], pc: int):
    if isinstance(obj, ast.Assign):
        for inst in assign(obj):
            instructions_list.append(inst.upper())
            pc += 1
    elif isinstance(obj, ast.Expr) and isinstance(obj.value, ast.Call):
        instructions_list.append(call(obj.value).upper())
        pc += 1
    elif isinstance(obj, ast.If):
        for inst in create_if(obj):
            instructions_list.append(inst.upper())
            pc += 1
    elif isinstance(obj, ast.For):
        for inst in create_for(obj):
            instructions_list.append(inst.upper())
            pc += 1
    elif isinstance(obj, ast.While):
        for inst in create_while(obj):
            instructions_list.append(inst.upper())
    return pc

def main() -> list:
    instructions_list: list = []
    pc: int = 1

    with open('programm.py', 'r') as file:
        tree = ast.parse(file.read())

    for obj in tree.body:
        pc = process_statement(obj, instructions_list, pc)

    return instructions_list

if __name__ == '__main__':
    instructions = main()
    with open('output.txt', 'w') as f:
        for index, instruction in enumerate(instructions, start=1):
            if "GOTO " in instruction:
                goto_i = instruction.index('GOTO ') + 5
                instruction = instruction[:goto_i] + f"{int(instruction[goto_i:]) + index:02d}"

            f.write(f'{index:02d} {instruction}\n')
