# -o-o-o-o- Simple Functions -o-o-o-o-

# This file goes over basic functions in Python simply.
#
#  # # # # KEY # # # #
#
# def      - keyword used to define a function in Python.
#            C:  int add(int a, int b) { return a + b; }
#            C#: static int Add(int a, int b) { return a + b; }
#            Py: def add(a, b):
#                    return a + b
#
#            No return type is written — Python figures it out at runtime.
#            No static keyword needed — functions are not inside a class.
#            A colon : is required at the end of the def line.
#            The function body is indented.
#
# return   - exits the function and optionally sends a value back to the caller.
#            Same concept as C and C#.
#            A function with no return statement returns None automatically.
#
# parameters - variables listed in the function's parentheses that receive
#            values when the function is called. No types needed.
#            eg. def greet(name):  — name is the parameter.
#
# default parameters - a parameter can have a default value.
#            If no argument is passed, the default is used.
#            eg. def power_of(number, power=2):
#            Same concept as default parameters in C#. Not available in C.
#
# return multiple values - Python functions can return more than one value
#            using a tuple. No equivalent in C or C#.
#            eg. return min_val, max_val
#
# if __name__ == "__main__": - the Python equivalent of the entry point.
#            Code inside this block only runs when the file is executed directly,
#            not when it is imported as a module.
#            Equivalent to static void Main() in C#, or int main() in C.
#
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
#


# A function that returns nothing (like void in C and C#)
def greet(name):
    print(f"Hello, {name}!")


# A function that returns a value
def add(a, b):
    return a + b


# A function that returns a float
def multiply(a, b):
    return a * b


# A function with a default parameter value
# If no argument is passed for 'power', it defaults to 2
def power_of(number, power=2):
    return number ** power


# A function that returns multiple values (unique to Python)
def get_min_max(numbers):
    return min(numbers), max(numbers)  # returns a tuple


# Entry point
if __name__ == "__main__":

    # Calling the void-like function
    greet("World")

    # Calling the function and storing the result
    total = add(5, 3)
    print(f"5 + 3 = {total}")

    # Calling the multiply function
    product = multiply(4.5, 2.0)
    print(f"4.5 * 2.0 = {product}")

    # Calling with and without the default parameter
    print(f"3 squared: {power_of(3)}")      # uses default power=2
    print(f"2 cubed:   {power_of(2, 3)}")   # overrides default

    # Unpacking multiple return values
    nums = [4, 1, 8, 2, 7]
    minimum, maximum = get_min_max(nums)
    print(f"\nMin: {minimum}, Max: {maximum}")
