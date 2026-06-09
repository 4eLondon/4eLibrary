# -o-o-o-o- Simple Loops (While) -o-o-o-o-

# This file goes over the while loop in Python simply.
#
#  # # # # KEY # # # #
#
# while    - a loop that repeats a block of code AS LONG AS a condition is true.
#            The condition is checked BEFORE each iteration.
#            Syntax is almost identical to C and C# but:
#              - no parentheses needed around the condition
#              - a colon : is required at the end of the while line
#              - indentation defines the loop body instead of { }
#
#            C / C#:              Python:
#            while (i < 5) {      while i < 5:
#                ...                  ...
#            }
#
# True     - boolean literal (capital T). while True: creates an infinite loop
#            that runs forever until a break statement exits it.
#            Equivalent to while (true) in C and C#.
#
# break    - exits the loop immediately, even if the condition is still true.
#            Same as C and C#.
#
# continue - skips the rest of the current iteration and re-checks the condition.
#            Same as C and C#.
#
# input()  - reads a line of user input as a string.
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
#
# Note: Always make sure the condition will eventually become False,
#       or use break — otherwise you get an infinite loop.
#

# Basic while loop
i = 0
print("Counting with while loop:")
while i < 5:
    print(f"  i = {i}")
    i += 1  # increment — without this the loop runs forever

# While loop with user input — keeps going until user types "quit"
print("\nType something (type 'quit' to stop):")
user_input = ""
while user_input != "quit":
    user_input = input("> ")
    if user_input != "quit":
        print(f"You typed: {user_input}")
print("Loop ended.")

# Infinite loop with break
count = 0
print("\nInfinite loop broken at 3:")
while True:
    print(f"  count = {count}")
    count += 1
    if count == 3:
        break  # exit when count reaches 3

# While loop with continue — skip even numbers
print("\nOdd numbers only (continue):")
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # skip even numbers
    print(f"  {n}")
