package main

import "fmt"

func reverseString(s string) string {
	// Convert the string to a slice of runes
	runes := []rune(s)

	// Reverse the slice using a loop
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	// Convert the reversed slice back to a string
	return string(runes)
}

func main() {
	s := "I Love U Vishu"
	reversed := reverseString(s)
	fmt.Println(reversed) // Output: !dlrow ,olleH
}
