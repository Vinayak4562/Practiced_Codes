package main

import "fmt"

func linearsearch(A []int, key int) int {
	for index := 0; index < len(A); index++ {
		if key == A[index] {
			return index
		}

	}
	return -1
}

func main() {
	A := []int{11, 22, 33, 44, 55, 66, 77, 88}
	fmt.Println(linearsearch(A, 777))
}
