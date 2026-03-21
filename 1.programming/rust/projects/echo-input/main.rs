// Project: echo input
// What it does: asks the user for their name and age, then prints them back
// Run: rustc main.rs -o echo && ./echo

use std::io::{self, Write};

fn main() {
    let mut name = String::new();
    let mut age = String::new();

    print!("Enter your name: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut name).unwrap();

    print!("Enter your age: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut age).unwrap();

    println!("\nYou entered:");
    println!("  Name: {}", name.trim());
    println!("  Age:  {}", age.trim());
}
