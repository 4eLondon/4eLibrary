// -o-o-o-o- Syntax (Variables) -o-o-o-o-

/* This file goes over variables in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * variable - a named storage location that holds a value which can change
 *            during the program. Same concept as in C.
 *
 * type     - every variable has a type that defines what kind of data it stores.
 *            C# is strongly typed — you cannot store a string in an int, etc.
 *            Same concept as C.
 *
 * =        - the assignment operator. Stores a value into a variable.
 *
 * Naming rules (C# and C share most of these):
 *   - Must start with a letter or underscore (_), not a number.
 *   - Cannot use reserved keywords (eg. int, class, return).
 *   - Case sensitive: myVar and myvar are different variables.
 *   - C# convention: use camelCase for local variables. eg. myVariable.
 *
 * Scope    - where a variable can be accessed. A variable declared inside {}
 *            only exists within those braces. Same concept as C.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * Differences from C:
 *   - C# has 'string' as a built-in type; C uses char arrays.
 *   - C# has 'bool' with true/false; C uses int (1/0).
 *   - C# variables cannot be used before being assigned (local scope).
 *   - C# supports 'var' for implicit typing (see syntax-init.cs).
 *
 * */

using System;

class Program {
    static void Main() {

        // Integer variable
        int score = 0;
        Console.WriteLine($"Initial score: {score}");

        score = 50; // reassigning
        Console.WriteLine($"Updated score: {score}");

        score = score + 10; // using the variable in an expression
        Console.WriteLine($"Score after +10: {score}");

        // Double variable
        double temperature = 36.6;
        Console.WriteLine($"\nTemperature: {temperature}");

        temperature = temperature - 1.5;
        Console.WriteLine($"Temperature after -1.5: {temperature}");

        // Boolean variable (true or false)
        bool isRunning = true;
        Console.WriteLine($"\nProgram running: {isRunning}");

        isRunning = false;
        Console.WriteLine($"Program running: {isRunning}");

        // String variable
        string playerName = "Hero";
        Console.WriteLine($"\nPlayer: {playerName}");

        playerName = "SuperHero"; // strings can be reassigned
        Console.WriteLine($"Player: {playerName}");

        // Char variable (single character, uses single quotes)
        char grade = 'A';
        Console.WriteLine($"\nGrade: {grade}");

        // Demonstrating scope — this variable only exists inside these braces
        {
            int localVar = 999;
            Console.WriteLine($"\nInside scope: localVar = {localVar}");
        }
        // Console.WriteLine(localVar); // ERROR: localVar does not exist out here

    }
}
