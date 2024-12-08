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
from .expressions import bin_op, call
from .constants import SUPPORTED_COMPARE_OPERATIONS, OPPOSITE_COMPARE

def process_statement(stmt) -> str | list[str]:
    if isinstance(stmt, ast.Assign):
        return assign(stmt)
    elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
        return call(stmt.value)
    elif isinstance(stmt, ast.If):
        return create_if(stmt)
    elif isinstance(stmt, ast.For):
        return create_for(stmt)
    else:
        raise NotImplementedError("Unsupported operation.")

def process_condition(obj: ast.If | ast.While):
    if isinstance(obj.test, ast.Compare):
        if type(obj.test.ops[0]) not in SUPPORTED_COMPARE_OPERATIONS:
            raise NotImplementedError(f"Operation {type(obj.test.ops[0])} is not implemented")
        if len(obj.test.comparators) > 1:
            raise NotImplementedError("Can't use more than 1 comparison in PBasic")
        if any([isinstance(obj.test.left, ast.Str), isinstance(obj.test.comparators[0], ast.Str)]):
            raise NotImplementedError("Can't compare strings in PBasic")

        left = str(obj.test.left.id) if isinstance(obj.test.left, ast.Name) else str(obj.test.left.value)
        right = str(obj.test.comparators[0].id) if isinstance(obj.test.comparators[0], ast.Name) else str(obj.test.comparators[0].value)

        return f'{left}{SUPPORTED_COMPARE_OPERATIONS[type(obj.test.ops[0])]}{right}'
    else:
        raise NotImplementedError("Can only use compare operations in conditions.")

def process_inverted_condition(obj: ast.While):
    """Used in loops to skip their first iteration if condition is not met."""
    if isinstance(obj.test, ast.Compare):
        if type(obj.test.ops[0]) not in SUPPORTED_COMPARE_OPERATIONS:
            raise NotImplementedError(f"Operation {type(obj.test.ops[0])} is not implemented")
        if len(obj.test.comparators) > 1:
            raise NotImplementedError("Can't use more than 1 comparison in PBasic")
        if any([isinstance(obj.test.left, ast.Str), isinstance(obj.test.comparators[0], ast.Str)]):
            raise NotImplementedError("Can't compare strings in PBasic")

        left = str(obj.test.left.id) if isinstance(obj.test.left, ast.Name) else str(obj.test.left.value)
        right = str(obj.test.comparators[0].id) if isinstance(obj.test.comparators[0], ast.Name) else str(obj.test.comparators[0].value)

        return f'{left}{OPPOSITE_COMPARE[SUPPORTED_COMPARE_OPERATIONS[type(obj.test.ops[0])]]}{right}'
    else:
        raise NotImplementedError("Can only use compare operations in conditions.")

def assign(obj: ast.Assign) -> list[str]:
    """Assign statement.

    Examples:
        1:: a = 10:
            obj.targets = [Name(id='a')], obj.value = Constant(value=10)
        2:: a = b = 10:
            obj.targets = [Name(id='a'), Name(id='b')], obj.value = Constant(value=10)
        3:: a = b:
            obj.targets = [Name(id='a')], obj.value = Name(id='b')
        4.1:: a, b = 10, 20:
            obj.targets = [Tuple(elts[Name(id='a'), Name(id='b')])],
            obj.value = [Tuple(elts[Constant(value=10), Constant(value=20)])]
        4.2:: a, b = c, 10:
            obj.targets = [Tuple(elts[Name(id='a'), Name(id='b')])],
            obj.value = [Tuple(elts[Name(id='c'), Constant(value=10)])]
        5:: a = 15 + 10:
            obj.targets = [Name(id='a')], obj.value = BinOp(left=Constant(value=15)
                                                            op=Add()
                                                            right=Constant(value=10)
        6:: a = input():
            obj.targets = [Name(id='a')]
            obj.value = Call(func=Name(id='input'), args=[], kwargs=[])
    """

    result = []
    for target in obj.targets:
        if isinstance(target, ast.Name):
            if isinstance(obj.value, ast.Constant):
                result.append(f"LET {target.id}={repr(obj.value.value).replace("'", '"')}")
            elif isinstance(obj.value, ast.Name):
                result.append(f"LET {target.id}={obj.value.id}")
            elif isinstance(obj.value, ast.BinOp):
                result.append(f"LET {target.id}={bin_op(obj.value)}")
            elif isinstance(obj.value, ast.Call):
                if obj.value.func.id == 'input':
                    result.append(f"INPUT {target.id}")
                else:
                    result.append(f"{target.id}={call(obj.value)}")
            elif isinstance(obj.value, ast.Compare):
                left = str(obj.value.left.id) if isinstance(obj.value.left, ast.Name) else str(obj.value.left.value)
                right = str(obj.value.comparators[0].id) if isinstance(obj.value.comparators[0], ast.Name) else str(obj.value.comparators[0].value)
                result.append(f"LET {target.id}={left}{SUPPORTED_COMPARE_OPERATIONS[type(obj.value.ops[0])]}{right}")
        elif isinstance(target, ast.Tuple) and isinstance(obj.value, ast.Tuple):
            for elt_name, elt_value in zip(target.elts, obj.value.elts):
                if isinstance(elt_value, ast.Constant):
                    result.append(f"LET {elt_name.id}={repr(elt_value.value).replace("'", '"')}")
                elif isinstance(elt_value, ast.Name):
                    result.append(f"LET {elt_name.id}={elt_value.id}")
    return result

def create_if(obj: ast.If) -> list[str]:
    result = []
    condition = ['IF']
    else_stmt = []
    if_stmt = []

    condition.append(process_condition(obj))

    for stmt in obj.orelse:
        res = process_statement(stmt)
        if isinstance(res, list):
            else_stmt.extend(res)
        else:
            else_stmt.append(res)

    for stmt in obj.body:
        res = process_statement(stmt)
        if isinstance(res, list):
            if_stmt.extend(res)
        else:
            if_stmt.append(res)

    if len(else_stmt) == 1 and len(if_stmt) == 1 and len(else_stmt[0]) + len(if_stmt[0]) <= 30:
        condition.append(f'THEN {if_stmt[0]}')
        result.append(" ".join(condition))
        result.append(f'ELSE {else_stmt[0]}')
    else:
        condition.append(f'THEN GOTO {len(else_stmt) + 2}')
        result.append(" ".join(condition))
        result.extend(else_stmt)
        result.append(f"GOTO {len(if_stmt) + 1}")
        result.extend(if_stmt)
        result.append("REM *ELSE EXIT*")

    return result

def create_for(obj: ast.For) -> list[str]:
    result = []
    body = []

    if not isinstance(obj.iter, ast.Call) or obj.iter.func.id != 'range' or obj.orelse:
        raise NotImplementedError("Can only use range() created iterators without else statement.")

    start = obj.iter.args[0].value if len(obj.iter.args) > 1 else 0
    end = obj.iter.args[1].value - 1 if len(obj.iter.args) > 1 else obj.iter.args[0].value - 1
    result.append(f"FOR {obj.target.id}={start} TO {end}")

    for stmt in obj.body:
        if isinstance(stmt, ast.Break):
            raise NotImplementedError("Can't use break statement.")
        body.append(process_statement(stmt))

    result.extend(body)
    result.append(f"NEXT {obj.target.id}")

    return result

def create_while(obj: ast.While) -> list[str]:
    result: list[str] = []
    condition: list[str] = ['IF']
    inverted_condition: list[str] = ['IF']
    body: list[str] = []

    condition.append(process_condition(obj))
    inverted_condition.append(process_inverted_condition(obj))

    for stmt in obj.body:
        if isinstance(stmt, ast.Break):
            raise NotImplementedError("Can't use break statement.")
        res = process_statement(stmt)
        if isinstance(res, list):
            body.extend(res)
        else:
            body.append(res)
    
    body.append(f"{" ".join(condition)} THEN GOTO {-len(body)}")
    body.append("REM *WHILE EXIT*")
    
    inverted_condition.append(f"THEN GOTO {len(body)}")

    result.append(" ".join(inverted_condition))
    result.extend(body)

    return result
