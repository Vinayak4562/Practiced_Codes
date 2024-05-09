package main

import "fmt"

func SS(A []int) {
	for i := 0; i < len(A)-1; i++ {
		min := i
		for j := i + 1; j < len(A); j++ {
			if A[min] > A[j] {
				min = j
			}
		}
		A[min], A[i] = A[i], A[min]
	}
}
func main() {
	A := []int{2, 6, 8, -5, 1, 9}
	fmt.Println("Befor sorting", A)
	SS(A)
	fmt.Println("After Sorting", A)

}
