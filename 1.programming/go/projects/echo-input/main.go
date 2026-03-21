// Project: echo input
// What it does: asks the user for their name and age, then prints them back
// Run: go run main.go

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter your name: ")
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)

	fmt.Print("Enter your age: ")
	age, _ := reader.ReadString('\n')
	age = strings.TrimSpace(age)

	fmt.Println("\nYou entered:")
	fmt.Println("  Name:", name)
	fmt.Println("  Age: ", age)
}
