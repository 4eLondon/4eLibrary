// -o-o-o-o- Datatype (Floating Points) -o-o-o-o-

/* This file goes over floating point data types in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * float   - a 32-bit decimal number. Requires an 'f' suffix on literals.
 *           eg. float x = 3.14f;
 *           Precise to ~7 digits. Equivalent to float in C.
 *
 * double  - a 64-bit decimal number. This is the DEFAULT decimal type in C#.
 *           eg. double x = 3.14;
 *           Precise to ~15-16 digits. Equivalent to double in C.
 *
 * decimal - a 128-bit decimal number. Requires an 'm' suffix on literals.
 *           eg. decimal x = 3.14m;
 *           Precise to ~28-29 digits. Best used for money/finance.
 *           No direct equivalent in C.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * {0}     - a format placeholder. Works like %f in C's printf.
 *           eg. Console.WriteLine("Value: {0}", myVar);
 *           You can also use string interpolation: $"Value: {myVar}"
 *
 * */

using System;

class Program {
    static void Main() {

        float   myFloat   = 3.14f;       // 32-bit decimal, note the 'f' suffix
        double  myDouble  = 3.14159265;  // 64-bit decimal, default decimal type
        decimal myDecimal = 3.14m;       // 128-bit decimal, note the 'm' suffix

        Console.WriteLine("Float value:   {0}", myFloat);
        Console.WriteLine("Double value:  {0}", myDouble);
        Console.WriteLine("Decimal value: {0}", myDecimal);

        // Showing precision differences
        float   precisionFloat   = 1.0f / 3.0f;
        double  precisionDouble  = 1.0 / 3.0;
        decimal precisionDecimal = 1.0m / 3.0m;

        Console.WriteLine("\nPrecision comparison for 1/3:");
        Console.WriteLine("Float:   {0}", precisionFloat);
        Console.WriteLine("Double:  {0}", precisionDouble);
        Console.WriteLine("Decimal: {0}", precisionDecimal);

    }
}
