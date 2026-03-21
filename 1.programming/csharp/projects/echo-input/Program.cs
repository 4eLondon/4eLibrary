// Project: echo input
// What it does: asks the user for their name and age, then prints them back
// Run: dotnet run (inside a dotnet console project)

using System;

class Program {
    static void Main() {
        Console.Write("Enter your name: ");
        string name = Console.ReadLine();

        Console.Write("Enter your age: ");
        string age = Console.ReadLine();

        Console.WriteLine("\nYou entered:");
        Console.WriteLine($"  Name: {name}");
        Console.WriteLine($"  Age:  {age}");
    }
}
