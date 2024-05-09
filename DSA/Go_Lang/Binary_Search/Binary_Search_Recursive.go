package main

import "fmt"

func binaryrecursive(A []int, key, l, r int) int {
	if l > r {
		return -1
	} else {
		mid := (l + r) / 2
		if key == A[mid] {
			return mid
		} else if key < A[mid] {
			return binaryrecursive(A, key, l, mid-1)
		} else if key > A[mid] {
			return binaryrecursive(A, key, mid+1, r)
		}
	}
	return 0
}

func main() {
	A := []int{25, 36, 65, 96, 88}
	b := len(A)
	f := binaryrecursive(A, 69, 0, b)
	fmt.Println("result:", f)

}
