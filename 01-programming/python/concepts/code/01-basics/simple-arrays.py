# -o-o-o-o- Simple Arrays (Lists) -o-o-o-o-

# This file goes over the Python equivalent of arrays simply.
#
#  # # # # KEY # # # #
#
# list     - Python's equivalent of an array. A list holds an ordered collection
#            of items. Unlike C and C# arrays, Python lists:
#              - can hold items of DIFFERENT types (eg. ints and strings together)
#              - are DYNAMIC — they grow and shrink automatically
#              - do not require a fixed size at declaration
#
#            C:  int arr[5] = {10, 20, 30, 40, 50};
#            C#: int[] arr = {10, 20, 30, 40, 50};
#            Py: arr = [10, 20, 30, 40, 50]
#
# []       - square brackets define a list literal.
#            eg. numbers = [1, 2, 3]
#
# index    - lists are zero-indexed. First element is at index 0.
#            Negative indexes count from the end: -1 is the last element.
#            eg. numbers[0] is the first, numbers[-1] is the last.
#
# len()    - returns the number of items in a list.
#            Equivalent to .Length in C# or manually tracking size in C.
#
# .append()  - adds an item to the END of the list.
# .insert()  - inserts an item at a specific index.
# .remove()  - removes the first occurrence of a value.
# .pop()     - removes and returns the item at a given index (default: last).
# .sort()    - sorts the list in place (ascending by default).
# .reverse() - reverses the list in place.
#
# for ... in - a loop that iterates over every item in a list.
#              Equivalent to foreach in C#.
#
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
#

# Declaring and initialising a list
numbers = [10, 20, 30, 40, 50]

# Accessing elements by index
print(f"First element:  {numbers[0]}")
print(f"Last element:   {numbers[-1]}")  # negative index counts from end
print(f"List length:    {len(numbers)}")

# Printing all elements with a for loop
print("\nAll elements (for loop):")
for i in range(len(numbers)):
    print(f"  numbers[{i}] = {numbers[i]}")

# Iterating directly over items (simpler, like foreach)
print("\nAll elements (for-in loop):")
for num in numbers:
    print(f"  {num}")

# Modifying a list
numbers.append(60)         # add to end
print(f"\nAfter append(60):    {numbers}")

numbers.insert(0, 5)       # insert 5 at index 0
print(f"After insert(0, 5): {numbers}")

numbers.remove(30)         # remove first occurrence of 30
print(f"After remove(30):   {numbers}")

numbers.pop()              # remove and return last element
print(f"After pop():        {numbers}")

# Sorting and reversing
numbers.sort()
print(f"\nAfter sort():       {numbers}")

numbers.reverse()
print(f"After reverse():    {numbers}")

# Mixed-type list (unique to Python — not possible in C or C#)
mixed = [1, "hello", 3.14, True]
print(f"\nMixed list: {mixed}")

# List slicing — extracting a portion of the list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"\nFull list:       {fruits}")
print(f"Slice [1:3]:     {fruits[1:3]}")  # index 1 up to (not including) 3
print(f"Slice [:2]:      {fruits[:2]}")   # from start up to index 2
print(f"Slice [2:]:      {fruits[2:]}")   # from index 2 to end
print(f"Slice [-2:]:     {fruits[-2:]}")  # last 2 elements
