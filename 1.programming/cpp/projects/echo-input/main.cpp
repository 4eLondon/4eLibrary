// Project: echo input
// What it does: asks the user for their name and age, then prints them back
// Run: g++ main.cpp -o echo && ./echo

#include <iostream>
#include <string>

int main() {
    std::string name, age;

    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    std::cout << "Enter your age: ";
    std::getline(std::cin, age);

    std::cout << "\nYou entered:" << std::endl;
    std::cout << "  Name: " << name << std::endl;
    std::cout << "  Age:  " << age << std::endl;

    return 0;
}
