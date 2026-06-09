// -o-o-o-o- Syntax (Initialisation) -o-o-o-o-

/* This file goes over variable declaration and initialisation in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * declaration     - creating a variable and giving it a name and type.
 *                   eg. int a;
 *                   Same concept as C.
 *
 * initialisation  - assigning a value to a variable at the time of declaration.
 *                   eg. int a = 10;
 *                   Same concept as C.
 *
 * = - the assignment operator. Stores a value in a variable.
 *     Same as in C.
 *
 * Data types in C# (compared to C):
 *
 *   int     - 32-bit integer.                    Same as int in C.
 *   long    - 64-bit integer.                    Same as long in C.
 *   float   - 32-bit decimal. Needs 'f' suffix.  Same as float in C.
 *   double  - 64-bit decimal.                    Same as double in C.
 *   char    - a single character.                Same as char in C.
 *   bool    - true or false. Written as bool.    Same idea as in C (C uses int).
 *   string  - a sequence of characters.          C# has a proper string type;
 *                                                C uses char arrays.
 *   decimal - 128-bit high-precision decimal.    No equivalent in C.
 *
 * var     - lets C# infer the type automatically based on the assigned value.
 *           eg. var x = 10; is treated as int x = 10;
 *           No equivalent in C.
 *
 * default values - unassigned class-level variables get a default value:
 *                  int = 0, double = 0.0, bool = false, string = null.
 *                  Local variables MUST be assigned before use in C#.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * */

using System;

class Program {
    static void Main() {

        // Declaration and initialisation of basic types
        int     myInt     = 42;
        long    myLong    = 1234567890123L; // 'L' suffix for long literals
        float   myFloat   = 3.14f;          // 'f' suffix required for float literals
        double  myDouble  = 3.14159265;
        char    myChar    = 'A';
        bool    myBool    = true;
        string  myString  = "Hello";
        decimal myDecimal = 99.99m;         // 'm' suffix for decimal literals

        // Printing each variable
        Console.WriteLine($"int:     {myInt}");
        Console.WriteLine($"long:    {myLong}");
        Console.WriteLine($"float:   {myFloat}");
        Console.WriteLine($"double:  {myDouble}");
        Console.WriteLine($"char:    {myChar}");
        Console.WriteLine($"bool:    {myBool}");
        Console.WriteLine($"string:  {myString}");
        Console.WriteLine($"decimal: {myDecimal}");

        // Using 'var' — type is inferred by the compiler
        var inferredInt    = 10;       // compiler knows this is int
        var inferredString = "World";  // compiler knows this is string
        Console.WriteLine($"\nvar int:    {inferredInt}");
        Console.WriteLine($"var string: {inferredString}");

        // Declaration without initialisation (must assign before use)
        int uninitialised;
        uninitialised = 100; // assigned before it is used below
        Console.WriteLine($"\nLate initialisation: {uninitialised}");

    }
}
