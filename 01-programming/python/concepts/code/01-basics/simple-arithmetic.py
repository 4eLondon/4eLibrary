# -o-o-o-o- Simple Arithmetic -o-o-o-o-

# This file goes over basic arithmetic operations in Python simply.
#
#  # # # # KEY # # # #
#
# +   - addition operator. Same as C and C#.
# -   - subtraction operator. Same as C and C#.
# *   - multiplication operator. Same as C and C#.
# /   - division operator. ALWAYS returns a float in Python, even for integers.
#       eg. 7 / 2 = 3.5   (NOT 3 like in C and C#)
#       This is different from C and C# where int / int = int.
# //  - integer (floor) division. Drops the decimal, like int / int in C and C#.
#       eg. 7 // 2 = 3
# %   - modulus operator. Returns the remainder of a division. Same as C and C#.
#       eg. 7 % 2 = 1
# **  - exponentiation (power) operator. Unique to Python.
#       eg. 2 ** 3 = 8  (2 to the power of 3)
#       No direct operator equivalent in C/C# (use pow() or Math.Pow()).
#
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
#            Equivalent to $"..." in C# or printf() in C.
#
# Note: Python integers have unlimited size — no overflow like in C or C#.
#

a = 10
b = 3

# Basic arithmetic
print(f"{a} + {b}  = {a + b}")    # Addition
print(f"{a} - {b}  = {a - b}")    # Subtraction
print(f"{a} * {b}  = {a * b}")    # Multiplication
print(f"{a} / {b}  = {a / b}")    # True division (always float)
print(f"{a} // {b} = {a // b}")   # Integer / floor division
print(f"{a} % {b}  = {a % b}")    # Modulus (remainder)
print(f"{a} ** {b} = {a ** b}")   # Exponentiation (10 to the power of 3)

# Division always returns a float in Python
print(f"\n6 / 2 = {6 / 2}")       # 3.0, not 3
print(f"6 // 2 = {6 // 2}")      # 3 (integer division)

# Compound assignment operators (shorthand)
x = 10
x += 5   # same as x = x + 5
print(f"\nx after += 5:  {x}")
x -= 3   # same as x = x - 3
print(f"x after -= 3:  {x}")
x *= 2   # same as x = x * 2
print(f"x after *= 2:  {x}")
x //= 4  # same as x = x // 4
print(f"x after //= 4: {x}")
x **= 2  # same as x = x ** 2
print(f"x after **= 2: {x}")

# Python integers have no overflow limit
big_number = 2 ** 100
print(f"\n2 ** 100 = {big_number}")
