# -o-o-o-o- Syntax (Variables) -o-o-o-o-

# This file goes over variables in Python simply.
#
#  # # # # KEY # # # #
#
# variable   - a named storage location that holds a value which can change.
#              Same concept as C and C#, but with key differences.
#
# No type declaration - Python is dynamically typed. You do NOT write the type
#              when declaring a variable. Python figures it out automatically.
#              C:  int score = 0;
#              C#: int score = 0;
#              Py: score = 0
#
# =          - the assignment operator. Stores a value into a variable.
#              Same as in C and C#.
#
# type()     - a built-in function that returns the type of a variable.
#              eg. type(score) returns <class 'int'>
#              Useful for checking what type Python assigned automatically.
#
# Dynamic typing - a variable's type can change when reassigned to a different
#              type. eg. x = 10 then x = "hello" is valid in Python.
#              This is NOT allowed in C or C#.
#
# Naming convention - Python uses snake_case for variable names.
#              eg. my_variable, player_name, high_score
#              C# uses camelCase. C uses either.
#
# Scope      - a variable declared inside a function only exists there.
#              Same concept as C and C#.
#
# print()    - prints text to the console with a newline at the end.
# f"..."     - f-string. Embeds variables directly in a string.
#

# Integer variable (no type needed)
score = 0
print(f"Initial score: {score}")

score = 50          # reassigning
print(f"Updated score: {score}")

score = score + 10  # using the variable in an expression
print(f"Score after +10: {score}")

# Float variable
temperature = 36.6
print(f"\nTemperature: {temperature}")

temperature = temperature - 1.5
print(f"Temperature after -1.5: {temperature}")

# Boolean variable (True or False — capital first letter in Python)
is_running = True
print(f"\nProgram running: {is_running}")

is_running = False
print(f"Program running: {is_running}")

# String variable
player_name = "Hero"
print(f"\nPlayer: {player_name}")

player_name = "SuperHero"
print(f"Player: {player_name}")

# Checking types with type()
print(f"\ntype(score):       {type(score)}")
print(f"type(temperature): {type(temperature)}")
print(f"type(is_running):  {type(is_running)}")
print(f"type(player_name): {type(player_name)}")

# Dynamic typing — a variable can change type (unique to Python)
x = 10
print(f"\nx is: {x} — type: {type(x)}")
x = "now a string"
print(f"x is: {x} — type: {type(x)}")

# Multiple assignment in one line
a, b, c = 1, 2, 3
print(f"\na={a}, b={b}, c={c}")
