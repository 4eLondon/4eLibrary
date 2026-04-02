#include <iostream>

int main() {
  std::string name;
  std::cout << "Please enter your name: ";
  std::cin >> name;
  std::cout << "Your name is " + name + ".";
  return 0;
}
