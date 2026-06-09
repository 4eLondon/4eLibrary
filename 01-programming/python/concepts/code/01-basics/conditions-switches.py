# -o-o-o-o- Conditions (Match / Switch) -o-o-o-o-

# This file goes over the Python equivalent of switch statements simply.
#
#  # # # # KEY # # # #
#
# match    - Python's equivalent of switch, introduced in Python 3.10.
#            Checks a value and runs the first matching case block.
#            If you are on Python 3.9 or earlier, use if/elif instead
#            (see the if/elif example at the bottom of this file).
#
# case     - defines a pattern to match against. Runs if the value matches.
#            Equivalent to case in C and C#.
#            A colon : is required at the end of the case line.
#
# case _   - the wildcard/default case. Runs if no other case matches.
#            Equivalent to default in C and C#.
#
# break    - NOT needed in Python's match statement. Python automatically
#            stops after the first matching case. There is no fall-through.
#            In C and C# you must write break manually.
#
# Indentation - Python uses indentation (4 spaces) instead of { } braces
#            to define code blocks.
#
# input()  - reads a line of user input. Always returns a string.
# int()    - converts a string to an integer.
# print()  - prints text to the console with a newline at the end.
#
# Note: match/case works with integers, strings, and more.
#

a = int(input("Please enter a number between 0 and 5: "))

match a:

    case 0:  # if the variable is equal to 0
        print("Variable a is equal to 0")
        # no break needed — Python stops here automatically

    case 1:
        print("Variable a is equal to 1")

    case 2:
        print("Variable a is equal to 2")

    case 3:
        print("Variable a is equal to 3")

    case 4:
        print("Variable a is equal to 4")

    case 5:
        print("Variable a is equal to 5")

    case _:  # default — runs if no other case matched
        print("\nERROR - Your number was outside of the range. "
              "Number must be equal to zero, five or between the two.")


# --- Matching strings ---
print()
day = input("Enter a day (mon/tue/wed/thu/fri/sat/sun): ").lower()

match day:
    case "mon" | "tue" | "wed" | "thu" | "fri":  # | means OR (match multiple values)
        print("Weekday")
    case "sat" | "sun":
        print("Weekend")
    case _:
        print("Unknown day")


# --- If you are on Python 3.9 or earlier, use if/elif instead of match ---
#
# a = int(input("Enter 0-5: "))
# if a == 0:
#     print("Zero")
# elif a == 1:
#     print("One")
# elif a == 2:
#     print("Two")
# ...
# else:
#     print("Out of range")
