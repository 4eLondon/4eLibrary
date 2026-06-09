# -o-o-o-o- Syntax (Initialisation) -o-o-o-o-

# This file goes over variable declaration and initialisation in Python simply.
#
#  # # # # KEY # # # #
#
# In Python, there is no separate declaration step. A variable is created
# the moment you assign a value to it. You never write the type.
#
# C:  int a;       <- declaration (no value yet)
#     a = 10;      <- initialisation
# C#: int a = 10;  <- declaration + initialisation together
# Py: a = 10       <- just assignment; Python handles everything else
#
# Data types Python uses automatically:
#
#   int     - whole numbers, any size.      eg. 42, -7, 1000000
#   float   - decimal numbers.              eg. 3.14, -0.5
#   complex - complex numbers.              eg. 2 + 3j   (no C/C# equivalent)
#   bool    - True or False (capitalised).  eg. True, False
#   str     - text / strings.               eg. "hello", 'world'
#   NoneType- the absence of a value.       eg. None  (like null in C#, NULL in C)
#
# type()   - returns the type of a variable. Useful for inspection.
#            eg. type(42) returns <class 'int'>
#
# int()    - converts a value to an integer.  eg. int("42") -> 42
# float()  - converts a value to a float.     eg. float("3.14") -> 3.14
# str()    - converts a value to a string.    eg. str(100) -> "100"
# bool()   - converts a value to a boolean.   eg. bool(0) -> False
#
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
#

# Basic type initialisation
my_int     = 42
my_float   = 3.14159265
my_bool    = True
my_string  = "Hello"
my_none    = None          # represents the absence of a value (like null)
my_complex = 2 + 3j        # complex number (unique to Python)

# Printing each variable and its type
print(f"int:     {my_int}      -> {type(my_int)}")
print(f"float:   {my_float} -> {type(my_float)}")
print(f"bool:    {my_bool}     -> {type(my_bool)}")
print(f"str:     {my_string}   -> {type(my_string)}")
print(f"None:    {my_none}     -> {type(my_none)}")
print(f"complex: {my_complex}   -> {type(my_complex)}")

# Type conversion (casting)
print("\nType conversion:")
print(f"int('99'):     {int('99')}    -> {type(int('99'))}")
print(f"float('3.5'):  {float('3.5')} -> {type(float('3.5'))}")
print(f"str(100):      {str(100)}     -> {type(str(100))}")
print(f"bool(0):       {bool(0)}  -> {type(bool(0))}")
print(f"bool(1):       {bool(1)}  -> {type(bool(1))}")

# Multiple assignment on one line
x, y, z = 10, 20.5, "Python"
print(f"\nx={x}, y={y}, z={z}")

# Assign the same value to multiple variables
a = b = c = 0
print(f"a={a}, b={b}, c={c}")
