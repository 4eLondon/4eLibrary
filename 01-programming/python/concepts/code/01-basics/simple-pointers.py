# -o-o-o-o- Simple Pointers (References) -o-o-o-o-

# This file goes over the Python equivalent of pointers simply.
#
#  # # # # KEY # # # #
#
# IMPORTANT: Python has NO pointers. You never write * or & like in C.
#            Python manages memory automatically (garbage collection).
#            However, understanding how Python handles values and references
#            is important and maps closely to the concept of pointers.
#
# id()     - returns the unique memory address (identity) of an object.
#            Equivalent to printing a pointer's address in C.
#            eg. id(x) shows where x lives in memory.
#
# Immutable types (behave like VALUE types / copied on assign):
#   int, float, bool, str, tuple
#   Assigning one to another gives an independent copy.
#   Equivalent to value types in C# (int, double, struct, etc.)
#   and regular variables in C.
#
# Mutable types (behave like REFERENCE types / shared on assign):
#   list, dict, set
#   Assigning one to another gives a reference to the SAME object in memory.
#   Changes to one affect the other.
#   Equivalent to reference types in C# (class, array) and pointers in C.
#
# .copy()  - creates a SHALLOW copy of a list (a new independent list).
#            Use this to avoid accidentally sharing a reference.
#            Equivalent to manually copying an array in C or C#.
#
# import copy; copy.deepcopy() - creates a DEEP copy (copies nested objects too).
#
# Passing to functions:
#   Immutable types are effectively passed by value — the function cannot
#   change the original.
#   Mutable types are effectively passed by reference — the function CAN
#   change the original.
#
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
#

import copy

# --- Immutable types (int) — behave like value types ---
a = 10
b = a        # b gets the same value, but they are independent
b = 99       # changing b does NOT affect a
print(f"a = {a}, b = {b}")  # a is still 10
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")   # different address after b = 99

# --- Mutable types (list) — behave like reference types / pointers ---
list1 = [1, 2, 3]
list2 = list1       # list2 points to the SAME list in memory
list2[0] = 99       # changing list2 ALSO changes list1
print(f"\nlist1 after changing list2[0]: {list1}")  # [99, 2, 3]
print(f"Same object? {list1 is list2}")             # True

# --- Making an independent copy ---
list3 = [1, 2, 3]
list4 = list3.copy()   # shallow copy — independent list
list4[0] = 99
print(f"\nlist3 after changing list4[0]: {list3}")  # [1, 2, 3] — unchanged
print(f"Same object? {list3 is list4}")             # False

# --- Passing mutable types to functions (like passing a pointer in C) ---
def append_zero(lst):
    lst.append(0)  # modifies the original list

my_list = [1, 2, 3]
print(f"\nBefore append_zero: {my_list}")
append_zero(my_list)
print(f"After append_zero:  {my_list}")  # [1, 2, 3, 0] — original changed

# --- Passing immutable types to functions (like passing by value in C) ---
def try_to_change(x):
    x = 999  # only changes the local variable, not the original

my_int = 10
print(f"\nBefore try_to_change: {my_int}")
try_to_change(my_int)
print(f"After try_to_change:  {my_int}")  # still 10 — original unchanged

# --- Deep copy for nested structures ---
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
deep    = copy.deepcopy(nested)

nested[0][0] = 99
print(f"\nOriginal nested: {nested}")   # [[99, 2], [3, 4]]
print(f"Shallow copy:    {shallow}")   # [[99, 2], [3, 4]] — inner list shared!
print(f"Deep copy:       {deep}")      # [[1, 2], [3, 4]]  — fully independent
