# -o-o-o-o- Syntax (Constants) -o-o-o-o-

# This file goes over constants in Python simply.
#
#  # # # # KEY # # # #
#
# constant   - a variable whose value should NOT be changed after it is set.
#              Python has no built-in const or readonly keyword like C and C#.
#              Instead, the convention is to name constants in ALL_CAPS.
#              Python trusts the programmer not to change them — it will not
#              enforce it or throw an error if you do.
#
# ALL_CAPS   - the naming convention for constants in Python.
#              eg. PI = 3.14159
#              This signals to other developers: "do not change this value."
#
# math.pi    - a built-in constant from Python's math module.
#              No need to define PI yourself.
#              Equivalent to Math.PI in C#.
#
# import math - imports Python's built-in math module, giving access to
#               mathematical constants and functions.
#               Equivalent to using System; in C# or #include <math.h> in C.
#
# print()    - prints text to the console with a newline at the end.
#
# f"..."     - f-string (formatted string). Embeds variables directly.
#              eg. f"Value: {PI}"
#              Equivalent to $"Value: {PI}" in C# or printf("%f", PI) in C.
#

import math

# Constants defined at the top of the file (ALL_CAPS by convention)
PI        = 3.14159265358979
MAX_SCORE = 100
APP_NAME  = "MyApp"

# Using the constants
print(f"App: {APP_NAME}")
print(f"Max score: {MAX_SCORE}")
print(f"Pi: {PI}")

# Using Python's built-in math.pi constant
circumference = 2 * math.pi * 5  # radius = 5
print(f"\nCircumference of circle (r=5): {circumference:.4f}")

# Other useful constants in the math module
print(f"\nmath.pi:  {math.pi}")
print(f"math.e:   {math.e}")   # Euler's number
print(f"math.inf: {math.inf}") # positive infinity

# Python won't stop you from doing this — but you shouldn't:
# MAX_SCORE = 999  # bad practice — treat ALL_CAPS as read-only
