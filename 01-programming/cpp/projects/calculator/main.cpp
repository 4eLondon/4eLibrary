#include <iostream>

void calculate(char sign, int num1, int num2) {
  if (sign == '+') {
    int sum = num1 + num2;
    std::cout << num1 << " + " << num2 << " = " << sum << std::endl;
  } else if (sign == '-') {
    int sum = num1 - num2;
    std::cout << num1 << " - " << num2 << " = " << sum << std::endl;
  } else if (sign == '*') {
    int sum = num1 * num2;
    std::cout << num1 << " * " << num2 << " = " << sum << std::endl;
  } else if (sign == '/') {
    int sum = num1 / num2;
    std::cout << num1 << " / " << num2 << " = " << sum << std::endl;
  } else {
    std::cout << "Invalid operator selected" << std::endl;
  };
};

int main() { return 0; }
