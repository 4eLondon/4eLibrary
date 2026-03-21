// Project: echo input
// What it does: asks the user for their name and age, then prints them back
// Run: javac EchoInput.java && java EchoInput

import java.util.Scanner;

public class EchoInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        String age = scanner.nextLine();

        System.out.println("\nYou entered:");
        System.out.println("  Name: " + name);
        System.out.println("  Age:  " + age);

        scanner.close();
    }
}
