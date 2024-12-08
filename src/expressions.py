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
from typing import Optional
from .constants import SUPPORTED_BINARY_OPERAIONS, BASE_OPERATIONS, SUPPORTED_FUNCTIONS

def bin_op(obj: ast.BinOp, operation_stack: Optional[list] = None) -> str:
    """Handle binary operation. Supports + - * /"""

    if type(obj.op) not in SUPPORTED_BINARY_OPERAIONS:
        raise NotImplementedError(f"Operation {type(obj.op)} is not implemented.")
    elif any([isinstance(obj.left, ast.Str), isinstance(obj.right, ast.Str)]):
        raise TypeError("Can't concatenate strings in PBasic")

    def process_bin_op_side(side, operation_stack, current_op):
        if isinstance(side, ast.BinOp):
            operation_stack.append(bin_op(side, operation_stack))
            result = "".join(operation_stack)
            operation_stack.clear()
            if type(current_op) in [ast.Mult, ast.Div] and any(['+' in result, '-' in result]):
                return f'({result})'
            elif type(current_op) == ast.Sub and not any(['*' in result, '/' in result]):
                return f'({result})'
            elif type(current_op) in [ast.Mult, ast.Div] and any(['*' in result, '/' in result]):
                return f'({result})'
            return result
        elif isinstance(side, ast.Call):
            return call(side)
        elif isinstance(side, ast.Name):
            return side.id
        else:
            return side.value

    if operation_stack is None:
        operation_stack = []

    left = process_bin_op_side(obj.left, operation_stack, obj.op)
    right = process_bin_op_side(obj.right, operation_stack, obj.op)

    return f"{left} {BASE_OPERATIONS[type(obj.op)]} {right}"


def call(obj: ast.Call) -> str:
    """Create a function call.

    If function is not supported, NotImplementedError will be raised.
    """

    func_name = obj.func.id

    if func_name == 'int_input':
        func_name = 'input'

    if func_name not in SUPPORTED_FUNCTIONS:
        raise NotImplementedError(f'Function {func_name} is not implemented.')

    result = func_name.upper() + " "

    for arg in obj.args:
        if isinstance(arg, ast.Name):
            result += arg.id
        elif isinstance(arg, ast.Constant):
            result += repr(arg.value).replace("'", '"')
        elif isinstance(arg, ast.BinOp):
            result += '(' + bin_op(arg) + ')'
        elif isinstance(arg, ast.Call):
            result += call(arg)

    return result
