# -o-o-o-o- Simple Enums -o-o-o-o-

# This file goes over basic enums in Python simply.
#
#  # # # # KEY # # # #
#
# enum     - short for "enumeration". A named set of related constant values.
#            Python enums require importing the Enum class from the enum module.
#            They are more powerful than C enums and similar to C# enums.
#
# from enum import Enum - imports the Enum base class from Python's built-in
#            enum module. You inherit from it to create your own enum.
#            No equivalent import needed in C (built-in keyword).
#            Equivalent to the built-in enum keyword in C#.
#
# class Direction(Enum): - defines an enum called Direction.
#            Each member is written as NAME = value.
#            Convention: enum member names are ALL_CAPS in Python.
#
# .name    - returns the string name of an enum member.
#            eg. Direction.NORTH.name -> "NORTH"
#
# .value   - returns the underlying value of an enum member.
#            eg. Direction.NORTH.value -> 1
#
# auto()   - automatically assigns incrementing integer values.
#            from enum import Enum, auto
#            Equivalent to the default 0, 1, 2... behaviour in C and C#.
#
# match    - commonly paired with enums to handle each case (Python 3.10+).
#            See conditions-switches.py. Use if/elif on older Python versions.
#
# print()  - prints text to the console with a newline at the end.
# f"..."   - f-string. Embeds variables directly in a string.
#

from enum import Enum, auto


# Enum with manually assigned values
class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST  = 3
    WEST  = 4


# Enum using auto() — values assigned automatically (1, 2, 3...)
class StatusCode(Enum):
    OK      = 200
    CREATED = 201
    ERROR   = 500


# Enum with auto() for automatic incrementing values
class Season(Enum):
    SPRING = auto()  # 1
    SUMMER = auto()  # 2
    AUTUMN = auto()  # 3
    WINTER = auto()  # 4


# Accessing an enum member
my_direction = Direction.NORTH

print(f"Direction: {my_direction}")          # Direction.NORTH
print(f"Name:      {my_direction.name}")     # NORTH
print(f"Value:     {my_direction.value}")    # 1

# Using an enum with match (Python 3.10+)
match my_direction:
    case Direction.NORTH:
        print("Heading North!")
    case Direction.SOUTH:
        print("Heading South!")
    case Direction.EAST:
        print("Heading East!")
    case Direction.WEST:
        print("Heading West!")

# Custom value enum
response = StatusCode.OK
print(f"\nStatus: {response.name} ({response.value})")

# auto() enum
print(f"\nSeasons:")
for season in Season:
    print(f"  {season.name} = {season.value}")

# Iterating over all members of an enum
print(f"\nAll directions:")
for direction in Direction:
    print(f"  {direction.name} = {direction.value}")

# Comparing enums
print(f"\nIs NORTH? {my_direction == Direction.NORTH}")  # True
print(f"Is SOUTH? {my_direction == Direction.SOUTH}")   # False
