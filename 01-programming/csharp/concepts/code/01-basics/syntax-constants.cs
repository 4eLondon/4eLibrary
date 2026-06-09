// -o-o-o-o- Syntax (Constants) -o-o-o-o-

/* This file goes over constants in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * constant - a variable whose value CANNOT be changed after it is set.
 *            Used for values that should never change during the program,
 *            such as mathematical constants, config values, or fixed sizes.
 *
 * const   - keyword used to declare a compile-time constant in C#.
 *           The value must be known at compile time (a fixed literal).
 *           C:  #define PI 3.14159    or    const float PI = 3.14159;
 *           C#: const double Pi = 3.14159;
 *
 *           Naming convention: C# constants use PascalCase or ALL_CAPS.
 *           eg. const int MaxSize = 100;
 *
 * readonly - a field that can only be assigned once — either at declaration
 *            OR in a constructor. Unlike const, its value can be set at runtime.
 *            No direct equivalent in standard C.
 *            eg. readonly int SessionId = GetId();
 *
 * Math.PI  - a built-in constant provided by C#'s Math class.
 *            No need to define PI yourself; C# has it already.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * Note: Trying to assign a new value to a const will cause a COMPILE ERROR.
 *       This is intentional — it protects values that should never change.
 *
 * */

using System;

class Program {

    // Constants declared at class level are accessible anywhere in the class
    const double Pi        = 3.14159265358979;
    const int    MaxScore  = 100;
    const string AppName   = "MyApp";

    static void Main() {

        // Using constants
        Console.WriteLine($"App: {AppName}");
        Console.WriteLine($"Max score: {MaxScore}");
        Console.WriteLine($"Pi: {Pi}");

        // Using C#'s built-in Math.PI constant
        double circumference = 2 * Math.PI * 5; // radius = 5
        Console.WriteLine($"\nCircumference of circle (r=5): {circumference:F4}");

        // Local constant (defined inside a method)
        const int DaysInWeek = 7;
        Console.WriteLine($"\nDays in a week: {DaysInWeek}");

        // This would cause a compile error:
        // DaysInWeek = 8; // ERROR: cannot assign to a constant

    }
}
