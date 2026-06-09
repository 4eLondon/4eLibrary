// -o-o-o-o- Simple Enums -o-o-o-o-

/* This file goes over basic enums in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * enum    - short for "enumeration". A named set of related constant values.
 *           Makes code more readable by replacing magic numbers with names.
 *           Declared similarly to C but must be outside a method.
 *           C:  enum Direction { NORTH, SOUTH, EAST, WEST };
 *           C#: enum Direction { North, South, East, West }
 *
 *           By default, enum values start at 0 and increase by 1.
 *           You can assign custom integer values manually.
 *
 * (int)   - casting an enum to its underlying integer value.
 *           eg. (int)Direction.North returns 0
 *
 * switch  - commonly paired with enums to handle each case.
 *           See conditions-switches.cs for switch basics.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * Note: In C#, enum names are accessed with the enum type name as a prefix.
 *       eg. Direction.North  (not just North like in C)
 *
 * */

using System;

// Enum declared outside the class (at namespace level)
enum Direction {
    North,  // = 0 by default
    South,  // = 1
    East,   // = 2
    West    // = 3
}

// Enum with custom assigned values
enum StatusCode {
    OK      = 200,
    Created = 201,
    Error   = 500
}

class Program {
    static void Main() {

        Direction myDirection = Direction.North;

        Console.WriteLine($"Direction: {myDirection}");           // Prints the name
        Console.WriteLine($"Int value: {(int)myDirection}");      // Prints the number (0)

        // Using an enum with a switch statement
        switch (myDirection) {
            case Direction.North:
                Console.WriteLine("Heading North!");
                break;
            case Direction.South:
                Console.WriteLine("Heading South!");
                break;
            case Direction.East:
                Console.WriteLine("Heading East!");
                break;
            case Direction.West:
                Console.WriteLine("Heading West!");
                break;
        }

        // Custom value enum
        StatusCode response = StatusCode.OK;
        Console.WriteLine($"\nStatus: {response} ({(int)response})");

    }
}
