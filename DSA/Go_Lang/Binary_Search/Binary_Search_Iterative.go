package main

import "fmt"

func binaryiteratirve(A []int, key int) int {
	left := 0
	right := len(A)
	for left <= right {
		mid := (left + right) / 2
		if key == A[mid] {
			return mid
		} else if key < A[mid] {
			right = mid - 1
		} else if key > A[mid] {
			left = left + 1
		}
	}
	return -1
}

func main() {
	A := []int{25, 33, 36, 65, 99, 258}
	fmt.Println(binaryiteratirve(A, 99))

}
