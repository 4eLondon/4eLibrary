use std::io;

fn main() {
    println!("Please enter a number: ");
    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("Failed to read input");

    println!("Please enter another number: ");
    let mut b = String::new();
    io::stdin().read_line(&mut b).expect("Failed to read input");

    let num: i32 = a.trim().parse().expect("Please enter a valid number");
    let num2: i32 = b.trim().parse().expect("Please enter a valid number");

    println!("{} + {} = {}", num, num2, num + num2);
    println!("{} - {} = {}", num, num2, num - num2);
    println!("{} * {} = {}", num, num2, num * num2);
    println!("{} / {} = {}", num, num2, num / num2);
}
