# -o-o-o-o- Simple Strings -o-o-o-o-

# This file goes over basic strings in Python simply.
#
#  # # # # KEY # # # #
#
# str      - Python's built-in string type. Even simpler than C#.
#            In C, strings are char arrays: char str[50];
#            In C#, strings are objects:    string str = "Hello";
#            In Python, strings are just:  str = "Hello"   or  str = 'Hello'
#            Single and double quotes both work in Python.
#
# f"..."   - f-string (formatted string). Embeds variables directly.
#            eg. f"Hello, {name}!"
#            Equivalent to $"Hello, {name}!" in C# or printf in C.
#
# +        - string concatenation. Joins two strings together. Same as C#.
#
# len()    - returns the number of characters in a string.
#            Equivalent to .Length in C#.
#
# Strings are immutable in Python — just like in C#. Methods return new strings.
#
# .upper()      - returns the string in UPPERCASE.
# .lower()      - returns the string in lowercase.
# .strip()      - removes whitespace from both ends (like .Trim() in C#).
# .replace()    - replaces all occurrences of a substring with another.
# .split()      - splits a string into a list based on a separator.
# .join()       - joins a list of strings into one string with a separator.
# .find()       - returns the index of the first occurrence (-1 if not found).
# .startswith() - returns True if the string starts with a given prefix.
# .endswith()   - returns True if the string ends with a given suffix.
# in            - checks if a substring exists in a string (returns True/False).
#                 Equivalent to .Contains() in C#.
#
# input()  - reads a line of user input as a string.
# print()  - prints text to the console with a newline at the end.
#

# Declaring strings
first_name = "John"
last_name  = 'Doe'   # single quotes work the same as double quotes

# Concatenation
full_name = first_name + " " + last_name
print("Full name: " + full_name)

# f-string interpolation (preferred in Python)
print(f"Hello, {first_name} {last_name}!")

# String length
print(f"\nLength of '{full_name}': {len(full_name)}")

# Case methods
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")

# Checking contents
print(f"\nContains 'John': {'John' in full_name}")   # True (uses 'in' keyword)
print(f"Starts with 'Jo': {full_name.startswith('Jo')}")
print(f"Ends with 'oe':   {full_name.endswith('oe')}")

# Replacing text
replaced = full_name.replace("John", "Jane")
print(f"\nAfter replace: {replaced}")

# Finding a character's index
index = full_name.find("D")
print(f"Index of 'D': {index}")

# Slicing a string (like Substring in C#)
# string[start:end]  — end is not included
sub = full_name[0:4]  # gets "John"
print(f"Slice [0:4]: {sub}")

# Splitting a string into a list
csv = "apple,banana,cherry"
fruits = csv.split(",")
print(f"\nSplit result: {fruits}")

# Joining a list back into a string
joined = " - ".join(fruits)
print(f"Joined: {joined}")

# Multi-line strings (using triple quotes)
multi = """This is a
multi-line
string."""
print(f"\nMulti-line string:\n{multi}")

# Getting user input (always returns a string)
user_input = input("\nEnter your name: ")
print(f"Hello, {user_input.strip()}!")   # strip() removes extra whitespace
