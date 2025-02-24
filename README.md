[![Progressbar95 Version](https://img.shields.io/badge/PB95--version-1.06-black?style=flat&labelColor=%23008f91)](https://progressbar95.fandom.com/wiki/1.06)

# PB95-PyToBasic
PyToBasic converts Python code to a language used in the game Progressbar95 called PBasic. Python code is more readable, allowing you to create scripts much faster.
Currently there are 4 functions: `print()`, `random()` RND in PB95, `let()` sets a variable, and `clear()` CLS in PB95.

> [!NOTE]
This is a fun little project that shouldn't be taken seriously. PBasic is very limited: you can't concatenate strings, create real functions, create classes, use most compare operators, create local variables, and much more. Take it as a small tool for experimenting, and wait for further updates if PBasic is updated. This repository is up-to-date with Progressbar95 v.1.06.

## Contents
- [Usage](#usage)
- [Documentation](#documentation)
- [Contribution](#contribution)
- [License](#license)

## Usage
> [!NOTE]
~~You need Python 3.12 to run the converter properly. The AST changes with each new version. I can't guarantee that it will work on older or newer versions. For example, 3.14 removed some deprecated variables that are being used.~~

> [!NOTE] Forget about that, I rewrote the program so that it doesnt use `ast` but instead uses OOP. - catamapp

You can download the source code from the latest release or clone the current branch using the `git clone` command.

Write your code in `main.py` and then execute the `main.py` file. The output of your PBasic program will be written in a new `output.txt` file.

Note that you need to manually input instructions in the game. There are save files for written code `/data/data/com.spookyhousestudios.progressbar95/app_data on Android`, but if you change them, the game will execute the code incorrectly, and your device must be rooted in order to access them. (which is a waste of time and makes your phone vulnerable)

# Documentation
This part will go over the operations you can do in the converter. You're expected to have a basic understanding of Python.

## Operations
Currently, you can only add, subtract, multiply, and divide as many numbers as you want. Brackets will be placed accordingly.

```python
# Implemented
10 + 5
a + b
a * (12 + 3) - 12
10 / (100 * 25)

# Not implemented
10 % 2
10 // 2
10 ** 2
```

### Boolean Operations
Boolean operations are not supported at all. You can only use the compare operators ==, !=, >, and <.

### Assignment
You can assign strings and numbers to variables. The converter will translate them to appropriate names. You can do math operations on numbers but can't concatenate strings.

```python
# Implemented
a = "PBasic"
a = 25 + 25
a, b = c, d
a = 5 == 5  # This is an edge case because you can't assign truth values yourself

# Not implemented
a = True
a = "P" + "Basic"
a = a or b
```

## Output/Input
### Input
You can output your variables, binary operations, or results of in-built functions. Multiple print arguments will split into multiple lines.

```python
# Implemented
print(20)
print(a)
print(a + b)
print(cos(12))

# Not implemented
print(f"F string {a}")
print(a or b)
```

### Input
You can get input from the user by using input(). Note that it will only properly work as a separate statement.

```python
# Implemented
a = input("Comments are ignored")

# Not implemented
print(input())
a, b = input()
```

If you need to get an integer from input, you can use an alias for it, since there's no type conversion in PBasic.

```python
from src.aliases import int_input

a = int_input()
```

## Conditionals
There are only 2 conditionals supported: `if`, `for` and `while`.

### If Statements
You can create as many if statements as you want. If they take single actions, the code will be optimized. Note that only compare operators are supported, since there are no real logical values in PBasic.

```python
if a > b:
    print(a)
    if a == 10:
        print(10)
elif 5 < 0:
    print("No way")
else:
    print(b)
```

### For Loops
You can create multiple for loops. You need to use range() as an iterable object. You can't use break or else statements. Note that in PBasic the first value in iteration is 1, but it's changed to 0 for compatibility. Make sure to specify the start number when necessary.

```python
# Implemented
for i in range(10):
    for j in range(1, 11):
        print(j)

# Not implemented
for letter in "any other iterable":
    print(letter)
```

### While Loops
While loops are done using if statement logic after conversion.

```python
num = 10
num_cl = num - 1

while num_cl > 0:
    num = num * num_cl
    num_cl = num_cl - 1

print(num)  # 3628800
```

Infinite loop example.

```python
TR = 1  # True
FL = 0  # False
var = TR  # This can be done simpler, but for the sake of this example, we will ignore it
while var == TR:
    print("True")
    if [condition]:
        var = FL
```

## Functions
Since there's no kind of return in PBasic, functions are just abstractions. Code inside them will be repeated after conversion. Functions must not accept any arguments and return None. Remember that there are no local variables in PBasic.

### In-built Functions
~~You can use everything said above plus functions provided in src.aliases.~~
> [!NOTE] In built functions have not been implemented yet.

```python
from src.aliases import *

cls()
for i in range(1, 17):
    background(i)

print(tan(30))
print(cos(30 + rnd(25)))
```

## Miscellaneous
Note that: 
1. You only have a maximum amount **40 characters in one line**. This is not being checked in most cases,  with instruction numbers not having a limit.
2. Local variables **don't exist**. Functions can only use global variables.
3. You can only use 1 comparison at a time in if statements.
4. You can't assign truth values to variables directly. You need to use something like ``TR = 1`` and ``FL = 0``, because they technically exist. (boolean alternative)
5. There is no `break` function to break an infinite loop, you must change the conditional variable of the infinite loop.
6. Game tip: sometimes your code will silence stop keys (e.g., pause, break) until completing. So make sure to save your hard-written code before executing, you may lose it otherwise!

# Contribution
If you want to improve the existing code or implement your own functionality, then go ahead. If you want to reach me, there's a Discord link in my profile.

# License
This project uses the MIT License. See [LICENSE](https://github.com/Lemon4ksan/PB95-PyToBasic/blob/master/LICENSE) for details.
