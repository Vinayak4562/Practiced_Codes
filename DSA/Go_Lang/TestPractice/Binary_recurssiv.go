package main

import "fmt"

func BSRE(A []int, key int, l int, r int) int {

	if l > r {
		return -1
	} else {
		mid := (l + r) / 2
		if key == A[mid] {
			return mid
		} else if key < A[mid] {
			return BSRE(A, key, l, mid-1)
		} else if key > A[mid] {
			return BSRE(A, key, mid+1, r)
		}
	}
	return 0
}

func main() {
	A := []int{11, 22, 33, 44, 55, 66, 77, 88}
	b := len(A)
	c := BSRE(A, 100, 0, b)
	fmt.Println(c)
}
