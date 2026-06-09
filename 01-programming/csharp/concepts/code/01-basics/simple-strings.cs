// -o-o-o-o- Simple Strings -o-o-o-o-

/* This file goes over basic strings in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * string  - a built-in type in C# for storing text. Far easier than C.
 *           In C, strings are char arrays with a null terminator: char str[50];
 *           In C#, string is a proper type: string name = "Hello";
 *           Strings in C# are immutable (cannot be changed after creation).
 *
 * $"..."  - string interpolation. Embed variables directly into a string.
 *           eg. $"Hello, {name}!" is cleaner than "Hello, " + name + "!"
 *
 * +       - string concatenation. Joins two strings together.
 *           eg. "Hello" + " World" = "Hello World"
 *
 * .Length - property that returns the number of characters in a string.
 *           eg. "Hello".Length returns 5
 *
 * .ToUpper()    - returns the string in ALL UPPERCASE.
 * .ToLower()    - returns the string in all lowercase.
 * .Trim()       - removes whitespace from the start and end of a string.
 * .Contains()   - returns true if a string contains a given substring.
 * .Replace()    - replaces all occurrences of one substring with another.
 * .Substring()  - extracts part of a string starting at a given index.
 * .Split()      - splits a string into an array based on a separator character.
 * .IndexOf()    - returns the index of the first occurrence of a character/string.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 * Console.ReadLine()  - reads a line of user input as a string.
 *
 * */

using System;

class Program {
    static void Main() {

        // Declaring and initialising strings
        string firstName = "John";
        string lastName  = "Doe";

        // Concatenation
        string fullName = firstName + " " + lastName;
        Console.WriteLine("Full name: " + fullName);

        // String interpolation (preferred in C#)
        Console.WriteLine($"Hello, {firstName} {lastName}!");

        // String properties and methods
        Console.WriteLine($"\nLength of '{fullName}': {fullName.Length}");
        Console.WriteLine($"Uppercase: {fullName.ToUpper()}");
        Console.WriteLine($"Lowercase: {fullName.ToLower()}");

        // Checking contents
        bool hasJohn = fullName.Contains("John");
        Console.WriteLine($"Contains 'John': {hasJohn}");

        // Replacing text
        string replaced = fullName.Replace("John", "Jane");
        Console.WriteLine($"After Replace: {replaced}");

        // Extracting a substring (start index, length)
        string sub = fullName.Substring(0, 4); // gets "John"
        Console.WriteLine($"Substring (0, 4): {sub}");

        // Finding a character's index
        int index = fullName.IndexOf('D');
        Console.WriteLine($"Index of 'D': {index}");

        // Splitting a string into parts
        string csv = "apple,banana,cherry";
        string[] fruits = csv.Split(',');
        Console.WriteLine("\nSplit result:");
        foreach (string fruit in fruits) {
            Console.WriteLine($"  {fruit}");
        }

        // Getting user input (always returns a string)
        Console.Write("\nEnter your name: ");
        string userInput = Console.ReadLine();
        Console.WriteLine($"Hello, {userInput.Trim()}!"); // Trim removes extra spaces

    }
}
