# -o-o-o-o- Conditions (If Else) -o-o-o-o-

# This file goes over how to do basic if else statements in Python simply.
#
#  # # # # KEY # # # #
#
# if       - checks a condition and runs the indented block if it is true.
#            No parentheses required around the condition (unlike C and C#).
#            A colon : is required at the end of the if line.
#            C:  if (a != 0) { ... }
#            C#: if (a != 0) { ... }
#            Py: if a != 0:
#
# elif     - short for "else if". Checks another condition if the previous
#            was false. Equivalent to else if in C and C#.
#
# else     - runs if none of the above conditions were true.
#            Same concept as C and C#. Ends with a colon.
#
# Indentation - Python uses indentation (4 spaces) to define code blocks.
#            There are NO curly braces { }. Getting indentation wrong causes
#            an IndentationError. This replaces { } from C and C#.
#
# !=       - not equal to operator. Same as C and C#.
# ==       - equal to operator. Same as C and C#.
# >  <     - greater than / less than. Same as C and C#.
# >= <=    - greater/less than or equal to. Same as C and C#.
# and      - logical AND. Equivalent to && in C and C#.
# or       - logical OR.  Equivalent to || in C and C#.
# not      - logical NOT. Equivalent to !  in C and C#.
#
# input()  - reads a line of user input. Always returns a string.
#            Equivalent to scanf() in C and Console.ReadLine() in C#.
# int()    - converts a string to an integer.
#            eg. int(input("Enter: "))
#
# print()  - prints text to the console with a newline at the end.
#

a = int(input("Please enter either 0 or 1: "))

# reads as -> if a is not equal to 0 -> run the indented block
if a != 0:
    print("Variable a is equal to 1. You get a treat")

# checks if the above condition was false and only runs if it was not true
else:
    print("Variable a is not equal to 1. You get no treats")


# --- elif example ---

score = int(input("\nEnter a score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# --- Combining conditions ---

x = int(input("\nEnter a number: "))

if x > 0 and x % 2 == 0:
    print("Positive and even")
elif x > 0 and x % 2 != 0:
    print("Positive and odd")
elif x < 0:
    print("Negative number")
else:
    print("Zero")
