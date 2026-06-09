# -o-o-o-o- Simple Loops (For) -o-o-o-o-

# This file goes over the for loop in Python simply.
#
#  # # # # KEY # # # #
#
# for loop - Python's for loop is different from C and C#.
#            It iterates directly over a sequence (list, range, string, etc.)
#            rather than using an initialiser/condition/increment.
#
#            C / C#:                        Python:
#            for (int i = 0; i < 5; i++)    for i in range(5):
#
# range()  - generates a sequence of numbers to loop over.
#            range(stop)           -> 0, 1, 2, ... stop-1
#            range(start, stop)    -> start, start+1, ... stop-1
#            range(start, stop, step) -> start, start+step, ... stop-1
#            eg. range(5)      -> 0 1 2 3 4
#                range(1, 6)   -> 1 2 3 4 5
#                range(0, 10, 2) -> 0 2 4 6 8
#
# for x in list: - iterates directly over a list (like foreach in C#).
#            No index needed. Simpler and more Pythonic.
#
# enumerate() - gives both the index AND the value when looping over a list.
#            eg. for i, val in enumerate(my_list):
#            Equivalent to a for loop with both i and arr[i] in C/C#.
#
# break    - exits the loop immediately. Same as C and C#.
# continue - skips the rest of the current iteration. Same as C and C#.
#
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
#

# Basic for loop counting up (0 to 4)
print("Counting up (0 to 4):")
for i in range(5):
    print(f"  i = {i}")

# Counting up from 1 to 5
print("\nCounting (1 to 5):")
for i in range(1, 6):
    print(f"  i = {i}")

# Counting down (5 to 1) using a negative step
print("\nCounting down (5 to 1):")
for i in range(5, 0, -1):
    print(f"  i = {i}")

# Counting by twos (0 to 10)
print("\nCounting by twos (0 to 10):")
for i in range(0, 11, 2):
    print(f"  i = {i}")

# Iterating directly over a list
fruits = ["apple", "banana", "cherry"]
print("\nIterating over a list:")
for fruit in fruits:
    print(f"  {fruit}")

# Using enumerate() to get index and value
print("\nWith index (enumerate):")
for i, fruit in enumerate(fruits):
    print(f"  [{i}] {fruit}")

# Using break to exit early
print("\nBreaking at 3:")
for i in range(10):
    if i == 3:
        break
    print(f"  i = {i}")

# Using continue to skip an iteration
print("\nSkipping 3 (continue):")
for i in range(6):
    if i == 3:
        continue
    print(f"  i = {i}")

# Iterating over a string character by character
print("\nLooping over a string:")
for char in "Hello":
    print(f"  {char}")
