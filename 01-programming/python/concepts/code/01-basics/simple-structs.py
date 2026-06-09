# -o-o-o-o- Simple Structs (Dataclasses) -o-o-o-o-

# This file goes over the Python equivalent of structs simply.
#
#  # # # # KEY # # # #
#
# IMPORTANT: Python has no struct keyword.
#            The closest equivalents are:
#              1. dataclass  — the recommended modern approach (Python 3.7+)
#              2. class      — a regular class (more flexible but more verbose)
#              3. namedtuple — a lightweight immutable option
#
# dataclass  - a special class decorator that auto-generates __init__, __repr__,
#              and other methods based on the fields you define.
#              Fields are declared with type hints (name: type = default).
#              from dataclasses import dataclass
#
# @dataclass - the decorator applied above a class to make it a dataclass.
#              A decorator modifies the behaviour of a class/function.
#              No equivalent in C. Similar to a struct with auto methods in C#.
#
# type hints - used in dataclasses to declare field types.
#              eg. name: str, age: int, height: float
#              Python does NOT enforce these at runtime — they are for
#              readability and tooling support only.
#
# .          - the dot operator accesses a field of a dataclass. Same as C and C#.
#
# Mutable    - dataclass instances are mutable by default (fields can be changed).
#              Use @dataclass(frozen=True) to make them immutable (like a const struct).
#
# __repr__   - a special method that defines how the object prints.
#              Dataclasses generate this automatically, so print(person)
#              shows a readable summary of all fields.
#
# print()    - prints text to the console with a newline at the end.
# f"..."     - f-string. Embeds variables directly in a string.
#

from dataclasses import dataclass
import math


# Defining a dataclass (equivalent of a struct)
@dataclass
class Person:
    name:   str
    age:    int
    height: float  # in metres

    # Dataclasses can have methods too (same as C# structs)
    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old, {self.height}m tall.")


# A dataclass with a method
@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


# Frozen dataclass — immutable (fields cannot be changed after creation)
@dataclass(frozen=True)
class Config:
    max_retries: int   = 3
    timeout:     float = 30.0
    debug:       bool  = False


# Creating an instance (no 'new' keyword needed in Python)
person1 = Person(name="Alice", age=30, height=1.65)

# Accessing fields with the dot operator
print(f"Name:   {person1.name}")
print(f"Age:    {person1.age}")
print(f"Height: {person1.height}m")

# Calling a method on the dataclass
person1.introduce()

# Dataclasses auto-generate a readable __repr__
print(f"\nFull repr: {person1}")

# Dataclasses are mutable by default — fields can be changed
person1.age = 31
print(f"Updated age: {person1.age}")

# Unlike C structs, assignment does NOT copy the data — it copies the reference
person2 = person1             # person2 points to the SAME object
person2.name = "Bob"
print(f"\nperson1.name after changing person2: {person1.name}")  # also "Bob"!

# To get an independent copy, use dataclasses.replace() or copy.copy()
from dataclasses import replace
person3 = replace(person1, name="Charlie")  # creates a new copy with name changed
print(f"person1.name: {person1.name}")      # unchanged
print(f"person3.name: {person3.name}")      # "Charlie"

# Point dataclass
p = Point(x=3.0, y=4.0)
print(f"\nPoint ({p.x}, {p.y})")
print(f"Distance from origin: {p.distance_from_origin()}")  # 5.0

# Frozen (immutable) dataclass
config = Config()
print(f"\nConfig: {config}")
# config.max_retries = 10  # ERROR: FrozenInstanceError — cannot change frozen fields
