# PB95-PyToBasic

PyToBasic converts python code to a language used in game Progressbar95 called PBasic.
Since python code is much more readable, you will create scripts much faster.

> [!NOTE]  
> This is a fun little project that shouldn't be taken seriously.
> PBasic is very limited, you can't concatonate strings, create real functions, create classes,
> use most compare operators, create local variables and much more. Take it as a small tool for experimenting.

## Contents

- [Usage](#usage)
- [Documentation](#documentation)
- [Contribution](#contribution)
- [License](#license)

## Usage

> [!NOTE]  
> You need python 3.12 to run converter properly. AST is changing with eachpyt new version.
> I can't guarantee that it will work on older or newer versions. E.g. 3.14 removed some deprecated vribles that are being used.

You can download the source code from latest release, or clone current branch using git clone command.

Write your code in programm.py and then execute main.py file. The output of your PBasic programm will be written in new output.txt file.

Note that you need to manually input instructions in game. There are save files for written code
(/data/data/com.spookyhousestudios.progressbar95/app_data on android), but if you change them, game will execute code incorrectly and your device must be rooted in order to access them.

## Documentation

This part will go over operations you can do in the converter. You're expected to have basic understanding of python.

### Binary Operations

Currently, you can only add, substract, multiply and divide as many numbers as you want.
Brackets will be placed accordingly.

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

### Boolean operations

Are not supported at all. You can only use compare operators ==, !=, >, <

### Assingment

You can assing string and numbers to variables. Converter will translate them to appropriate names. You can do math operations on numbers, but can't concatonate strings.

```python
# Implemented
a = "PBasic"
a = 25 + 25
a, b = c, d
a = 5 == 5  # This is an edge case, because you can't assign truth values yourself

# Not implemented
a = True
a = "P" + "Basic"
a = a or b
```

### Print

You can output your variables, binary operations or results of in-build functions. Multiple print arguments will split into multiple lines.

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

You can get input from user by using input(). Note that it will only properly work as a separate statement.

```python
# Implemented
a = input("Comments are ignored")

# Not implemented
print(input())
a, b = input()
```

If you need to get integer from input, you can use alias for it, since there's no type convertion in PBasic.

```python
from src.aliases import int_input

a = int_input()
```

### If statemets

You can create as many if statements as you want. If they take single actions, code will be optimised.
Note that only compare operator are supported, since there're no real logical values in PBasic.

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

### For loops

You can create multiple for loops. You need to use range() as an iterable object. You can't use break or else statements.
Note that in PBasic the first value in iteration is 1, but it's changed to 0 for compatibility. Make sure to specify the start number when neccessary.

```python
# Implemented
for i in range(10):
    for j in range(1, 11):
        print(j)

# Not implemented
for letter in "any other iterable":
    print(letter)
```

### While loops

While loops are done using if statement logic after convertion.

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

### Functions

Since there's no kind of return in PBasic, functions are just abstraction. Code inside them will be repeated after convertion. Functions must not accept any arguments and return None. Remember that there're not any local variables in PBasic.

### Inbuild Functions

You can use everything said above plus functions provided in src.aliases.

```python
from src.aliases import *

cls()
for i in range(1, 17):
    background(i)

print(tan(30))
print(cos(30 + rnd(25)))
```

### Misc

Note that that you can only type 40 characters in one line. This is not being checked in most cases. Instruction numbers don't have a limit.

Local variables don't exist. Functions can only use global variables.

You can only use 1 comparison at the time in if statement.

You can't assign truth values to variables directly. You need to use something like ``TR = 1`` and ``FL = 0``, because they technically exist.

Since you can't use break statement, you must change conditional variable of the infinite loop.

Game tip, sometimes your code will silence stop keys (e.g. pause, break) until completing, so make sure to save your hard written code before
executing. You may loose it otherwise!

## Contribution

If you want to improve already existing code or implement your own functionality, then go ahead. If you want to reach me, there's a Discord link in my profile.

## License

This project uses MIT License. See [LICENSE](https://github.com/Lemon4ksan/PB95-PyToBasic/blob/master/LICENSE) for details.
