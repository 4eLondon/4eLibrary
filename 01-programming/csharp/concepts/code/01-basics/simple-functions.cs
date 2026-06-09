// -o-o-o-o- Simple Functions -o-o-o-o-

/* This file goes over basic functions in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * function / method - a reusable block of code that performs a specific task.
 *           In C#, functions are called "methods" and must live inside a class.
 *           In C, functions live freely outside of any class.
 *
 * static  - means the method belongs to the class itself, not an instance of it.
 *           Methods called from Main() must be static (or Main must create an object).
 *           eg. static void MyMethod() { ... }
 *
 * void    - the return type meaning the function returns nothing.
 *           Same as void in C.
 *
 * return  - exits the function and optionally sends a value back to the caller.
 *           eg. return 42;
 *           Same as in C.
 *
 * int / double / string - return types. The type before the method name tells
 *           C# what kind of value the method will return.
 *           eg. static int Add(int a, int b) { return a + b; }
 *
 * parameters - variables listed in the method's parentheses that receive values
 *           when the method is called.
 *           eg. static void Greet(string name) — name is the parameter.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * Note: Unlike C, you do NOT need to forward-declare functions in C#.
 *       Methods can be defined in any order inside the class.
 *
 * */

using System;

class Program {

    // A void method - does something but returns nothing
    static void Greet(string name) {
        Console.WriteLine($"Hello, {name}!");
    }

    // A method that returns an integer
    static int Add(int a, int b) {
        return a + b;
    }

    // A method that returns a double
    static double Multiply(double a, double b) {
        return a * b;
    }

    // A method with a default parameter value
    // If no argument is passed, power defaults to 2
    static double PowerOf(double number, int power = 2) {
        double result = 1;
        for (int i = 0; i < power; i++) {
            result *= number;
        }
        return result;
    }

    static void Main() {

        // Calling the void method
        Greet("World");

        // Calling the int method and storing the result
        int sum = Add(5, 3);
        Console.WriteLine($"5 + 3 = {sum}");

        // Calling the double method
        double product = Multiply(4.5, 2.0);
        Console.WriteLine($"4.5 * 2.0 = {product}");

        // Calling with and without the default parameter
        Console.WriteLine($"3 squared:  {PowerOf(3)}");     // uses default power = 2
        Console.WriteLine($"2 cubed:    {PowerOf(2, 3)}");  // overrides default

    }
}
