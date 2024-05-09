package main

import "fmt"

func BinaryIterative(A []int, key int) int {
	l := 0
	r := len(A)
	for l <= r {
		mid := (l + r) / 2
		if key == A[mid] {
			return mid
		} else if key < A[mid] {
			r = mid - 1
		} else if key > A[mid] {
			l = l + 1
		}
	}
	return -1
}

func main() {
	A := []int{11, 22, 33, 44, 55, 66, 77, 88}
	b := BinaryIterative(A, 100)
	fmt.Println(b)
}
