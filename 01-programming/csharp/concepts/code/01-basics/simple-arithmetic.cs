// -o-o-o-o- Simple Arithmetic -o-o-o-o-

/* This file goes over basic arithmetic operations in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * +  - addition operator
 * -  - subtraction operator
 * *  - multiplication operator
 * /  - division operator
 *    Note: dividing two integers gives an integer result (remainder dropped).
 *          eg. 7 / 2 = 3 (not 3.5). Cast to double for decimal result.
 * %  - modulus operator. Returns the remainder of a division.
 *    eg. 7 % 2 = 1
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * $"..."  - string interpolation. Lets you embed variables directly in a string.
 *           eg. $"Result: {a + b}"
 *           Equivalent to printf("Result: %i", a + b) in C.
 *
 * (double) - casting. Converts an integer to a double for decimal division.
 *            eg. (double)a / b
 *            Same concept as casting in C.
 *
 * */

using System;

class Program {
    static void Main() {

        int a = 10;
        int b = 3;

        // Basic arithmetic
        Console.WriteLine($"{a} + {b} = {a + b}");   // Addition
        Console.WriteLine($"{a} - {b} = {a - b}");   // Subtraction
        Console.WriteLine($"{a} * {b} = {a * b}");   // Multiplication
        Console.WriteLine($"{a} / {b} = {a / b}");   // Integer division (remainder dropped)
        Console.WriteLine($"{a} % {b} = {a % b}");   // Modulus (remainder)

        // Casting to get a decimal result from division
        double decimalResult = (double)a / b;
        Console.WriteLine($"\n{a} / {b} as decimal = {decimalResult}");

        // Compound assignment operators (shorthand)
        int x = 10;
        x += 5;  // same as x = x + 5
        Console.WriteLine($"\nx after += 5: {x}");
        x -= 3;  // same as x = x - 3
        Console.WriteLine($"x after -= 3: {x}");
        x *= 2;  // same as x = x * 2
        Console.WriteLine($"x after *= 2: {x}");
        x /= 4;  // same as x = x / 4
        Console.WriteLine($"x after /= 4: {x}");

    }
}
