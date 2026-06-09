// -o-o-o-o- Syntax (Hello World) -o-o-o-o-

/* This file goes over the basic Hello World program in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * using System; - imports the System namespace which contains core C# tools
 *                 such as Console (for printing to the screen).
 *                 Equivalent to #include <stdio.h> in C.
 *
 * namespace     - a way to organise and group related code. C# code lives inside
 *                 namespaces. No direct equivalent in C.
 *
 * class         - in C#, all code must live inside a class. The entry point class
 *                 is typically named 'Program'. No equivalent in C.
 *
 * static void Main() - the entry point of a C# program. The runtime starts here.
 *                      Equivalent to int main() in C.
 *                      'static' means it belongs to the class, not an instance.
 *                      'void' means it returns nothing (unlike int main() in C).
 *
 * Console.WriteLine() - prints text to the console followed by a new line.
 *                       Equivalent to printf("Hello, World!\n") in C.
 *
 * Console.Write()     - prints text WITHOUT a trailing new line.
 *                       Equivalent to printf("Hello, World!") in C (no \n).
 *
 * // - single-line comment. Same as in C.
 *
 * */

using System;

class Program {
    static void Main() {

        // Print Hello World to the console
        Console.WriteLine("Hello, World!");

    }
}
