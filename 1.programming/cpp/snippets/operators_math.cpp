#include <iostream>

int main() {
  int num, num2;
  std::cout << "Please enter a number: ";
  std::cin >> num;
  std::cout << "Please enter another number: ";
  std::cin >> num2;

  std::cout << num << " + " << num2 << " = " << num + num2 << "\n";
  std::cout << num << " - " << num2 << " = " << num - num2 << "\n";
  std::cout << num << " * " << num2 << " = " << num * num2 << "\n";
  std::cout << num << " / " << num2 << " = " << num / num2 << "\n";
  return 0;
}
