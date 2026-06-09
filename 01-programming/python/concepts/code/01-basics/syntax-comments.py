# -o-o-o-o- Syntax (Comments) -o-o-o-o-

# This file goes over the different types of comments in Python simply.
#
#  # # # # KEY # # # #
#
# #         - single-line comment. Everything after # on that line is ignored.
#             Equivalent to // in C and C#.
#             There is no /* */ multi-line comment symbol in Python.
#
# """ ... """ or ''' ... ''' - a multi-line string used as a comment.
#             Technically these are string literals that are not assigned
#             to anything, so Python ignores them. They are widely used
#             as multi-line comments and as docstrings (see below).
#             Equivalent to /* */ in C and C#.
#
# docstring  - a """ string placed immediately inside a function, class,
#              or module to describe what it does. Python can read these
#              at runtime using the __doc__ attribute.
#              Similar to /// XML doc comments in C#.
#              No equivalent in C.
#
# Note: Good comments explain WHY, not just WHAT.
#       Comments do not affect how the program runs.
#

# This is a single-line comment
print("Comments do not affect output.")

"""
This is a multi-line string used as a comment.
It can span as many lines as needed.
Python ignores it because it is not assigned to anything.
"""

print("Multi-line string comments work fine in Python.")


def greet(name):
    """
    This is a docstring — it describes the function.
    It is readable at runtime via greet.__doc__
    
    Parameters:
        name (str): The name to greet.
    
    Returns:
        str: A greeting string.
    """
    return f"Hello, {name}!"  # inline comment: returns a greeting


message = greet("World")
print(message)

# You can read a docstring at runtime
print(greet.__doc__)

# print("This line is commented out and will not run.")
