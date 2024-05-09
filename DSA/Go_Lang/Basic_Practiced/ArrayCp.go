package main

import "fmt"

func main() {
	src := []int{1, 2, 3, 4, 5, 6}
	dest := make([]int, len(src))
	// num := copy(src, dest) it will copy dest to src
	num := copy(dest, src)
	fmt.Println(src, dest, num)

	src1 := []int{1, 2, 3, 4, 5, 6}
	dest1 := make([]int, 2)
	num1 := copy(dest1, src1)
	fmt.Println(src1, dest1, num1)

}
