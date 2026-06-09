# -o-o-o-o- Simple Loops (Do While) -o-o-o-o-

# This file goes over the Python equivalent of a do-while loop simply.
#
#  # # # # KEY # # # #
#
# IMPORTANT: Python does NOT have a do-while loop keyword.
#            The closest equivalent is a while True: loop with a break at the end.
#            This guarantees the code runs AT LEAST ONCE before checking the
#            condition, which is exactly how do-while works in C and C#.
#
#            C / C#:                     Python equivalent:
#            do {                        while True:
#                // code                    # code
#            } while (condition);           if not condition:
#                                               break
#
# while True: - creates a loop that runs forever until a break statement exits it.
#
# break    - exits the loop immediately.
#            Same concept as C and C#. Used here to replicate do-while behaviour.
#
# if not condition: break - the condition check at the END of the loop body.
#            This is what makes it behave like a do-while.
#
# input()  - reads a line of user input as a string. Always returns a string.
#            Equivalent to scanf() in C and Console.ReadLine() in C#.
# int()    - converts a string to an integer.
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
#

# Basic do-while equivalent: runs at least once
i = 0
print("Counting with do-while equivalent:")
while True:
    print(f"i = {i}")
    i += 1
    if not (i < 5):  # condition check at the END (do-while behaviour)
        break

# More readable version using a flag
print("\nSame loop, cleaner style:")
i = 0
while True:
    print(f"i = {i}")
    i += 1
    if i >= 5:
        break

# Practical example: input validation
# Keeps asking until the user enters a number between 1 and 10
print()
while True:
    user_input = int(input("Enter a number between 1 and 10: "))

    if 1 <= user_input <= 10:
        break  # valid input — exit the loop

    print("Invalid. Please try again.")

print(f"You entered: {user_input}")
