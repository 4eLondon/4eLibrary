# -o-o-o-o- Datatype (Floating Points) -o-o-o-o-

# This file goes over floating point data types in Python simply.
#
#  # # # # KEY # # # #
#
# float    - Python's only built-in floating point type.
#            It is a 64-bit double-precision decimal number.
#            Equivalent to double in C and C#. There is no separate float/double
#            distinction in Python — float covers both roles.
#            eg. x = 3.14
#
# complex  - Python's built-in complex number type (real + imaginary).
#            Written with a 'j' suffix for the imaginary part.
#            eg. z = 2 + 3j
#            No equivalent in standard C or C#.
#
# Decimal  - a high-precision decimal type from Python's decimal module.
#            Similar to decimal in C# or using fixed-point arithmetic.
#            Best used for financial/monetary calculations where float
#            rounding errors are not acceptable.
#            eg. from decimal import Decimal; x = Decimal("3.14")
#            Note: always pass the value as a STRING to Decimal() to avoid
#            floating point errors being baked in before Decimal sees the value.
#
# round()  - built-in function to round a float to a given number of decimals.
#            eg. round(3.14159, 2) -> 3.14
#
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
# :.Nf     - format specifier inside an f-string to show N decimal places.
#            eg. f"{value:.4f}" shows 4 decimal places.
#

from decimal import Decimal

# Basic float (Python's default decimal type — 64-bit double precision)
my_float = 3.14
print(f"Float value:   {my_float}")
print(f"Type:          {type(my_float)}")

# Python floats are always 64-bit (no need for a separate double type)
big_float = 3.14159265358979
print(f"\nHigh precision float: {big_float}")

# Floating point precision quirk (same in all languages)
print(f"\n0.1 + 0.2 = {0.1 + 0.2}")           # not exactly 0.3 due to binary representation
print(f"Rounded:   {round(0.1 + 0.2, 2)}")    # use round() to fix display

# Complex numbers (unique to Python)
my_complex = 2 + 3j
print(f"\nComplex number: {my_complex}")
print(f"Real part:      {my_complex.real}")
print(f"Imaginary part: {my_complex.imag}")

# Decimal for precise arithmetic (eg. money)
price   = Decimal("19.99")  # always pass as a string
tax     = Decimal("0.15")
total   = price * (1 + tax)
print(f"\nPrice:  {price}")
print(f"Tax:    {tax * 100}%")
print(f"Total:  {total}")

# Precision comparison for 1/3
float_third   = 1 / 3
decimal_third = Decimal("1") / Decimal("3")
print(f"\n1/3 as float:   {float_third}")
print(f"1/3 as Decimal: {decimal_third}")

# Formatting floats in output
value = 3.14159265
print(f"\n2 decimal places: {value:.2f}")
print(f"4 decimal places: {value:.4f}")
print(f"Scientific:       {value:.2e}")
