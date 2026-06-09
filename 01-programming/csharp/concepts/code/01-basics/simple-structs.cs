// -o-o-o-o- Simple Structs -o-o-o-o-

/* This file goes over basic structs in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * struct  - short for "structure". A custom data type that groups related
 *           variables (called fields) together under one name.
 *           Works similarly to C structs but with some important differences.
 *
 *           C:  struct Person { char name[50]; int age; };
 *           C#: struct Person { public string Name; public int Age; }
 *
 * public  - an access modifier. Makes a field visible and usable from outside
 *           the struct. Without it, fields are private and inaccessible.
 *           No direct equivalent in basic C (all C struct fields are accessible).
 *
 * .       - the dot operator accesses a field of a struct.
 *           eg. person.Name
 *           Same as in C.
 *
 * value type - structs in C# are VALUE types. Assigning a struct copies all
 *              its data, just like assigning a primitive (int, double, etc.).
 *              This is the same behaviour as C structs.
 *
 * class   - similar to a struct but a REFERENCE type. Classes are better for
 *           complex objects. Structs are best for small, simple data groupings.
 *           See simple-classes.cs if available.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * Note: Structs can also have methods and constructors in C#,
 *       which is not possible in basic C.
 *
 * */

using System;

// Struct declared outside the class (at namespace level)
struct Person {
    public string Name;
    public int    Age;
    public float  Height; // in metres

    // Structs in C# can have methods (unlike C)
    public void Introduce() {
        Console.WriteLine($"Hi, I am {Name}, {Age} years old, {Height}m tall.");
    }
}

// A more complex struct example
struct Point {
    public double X;
    public double Y;

    // Method to calculate distance from the origin (0, 0)
    public double DistanceFromOrigin() {
        return Math.Sqrt(X * X + Y * Y);
    }
}

class Program {
    static void Main() {

        // Creating and filling a struct
        Person person1;
        person1.Name   = "Alice";
        person1.Age    = 30;
        person1.Height = 1.65f;

        // Accessing struct fields with the dot operator
        Console.WriteLine($"Name:   {person1.Name}");
        Console.WriteLine($"Age:    {person1.Age}");
        Console.WriteLine($"Height: {person1.Height}m");

        // Calling a method on the struct
        person1.Introduce();

        // Structs are VALUE types — assignment copies the data
        Person person2 = person1;  // person2 gets a full copy of person1
        person2.Name = "Bob";      // changing person2 does NOT affect person1
        Console.WriteLine($"\nperson1.Name: {person1.Name}"); // still "Alice"
        Console.WriteLine($"person2.Name: {person2.Name}");   // "Bob"

        // Point struct example
        Point p = new Point();
        p.X = 3.0;
        p.Y = 4.0;
        Console.WriteLine($"\nPoint ({p.X}, {p.Y})");
        Console.WriteLine($"Distance from origin: {p.DistanceFromOrigin()}"); // 5.0

    }
}
