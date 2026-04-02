package main

import "fmt"

func main() {
	var num int
	var num2 int
	fmt.Println("Please enter a number: ")
	fmt.Scanln(&num)
	fmt.Println("Please enter another number: ")
	fmt.Scanln(&num2)

	fmt.Println(num, " + ", num2, " = ", num+num2)
	fmt.Println(num, " - ", num2, " = ", num-num2)
	fmt.Println(num, " * ", num2, " = ", num*num2)
	fmt.Println(num, " / ", num2, " = ", num/num2)
}
