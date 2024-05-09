package main

import "fmt"

func BL(A []int, key int) int {

	for index := 0; index < len(A); index++ {
		if key == A[index] {
			return index
		}
	}
	return -1
}

func main() {
	A := []int{11, 22, 33, 44, 55, 66, 77, 88, 99}
	fmt.Println(BL(A, 333))
}
