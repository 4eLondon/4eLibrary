package main

import "fmt"

func main() {
	var name string
	fmt.Println("Please enter your name: ")
	fmt.Scanln(&name)
	fmt.Println("You entered ", name)
}
