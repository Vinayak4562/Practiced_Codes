package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	t := x
	r := 0
	for x > 0 {
		r = r*10 + x%10
		x /= 10
	}
	return t == r
}

func main() {
	// a := isPalindrome(121)
	// fmt.Println(a)
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(123))
	fmt.Println(isPalindrome(1212))
	fmt.Println(isPalindrome(1221))
}
