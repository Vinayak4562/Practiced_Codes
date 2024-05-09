package main

import (
	"fmt"
)

func removeDuplicates(nums []int) int {
	i := 1
	for i < len(nums) {
		if nums[i] == nums[i-1] {
			nums = append(nums[:i], nums[i+1:]...)
		} else {
			i++
		}
	}
	// fmt.Println(i)
	return i
}

func main() {
	nums := []int{1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 8}
	// removeDuplicates(nums)
	// fmt.Println(nums)
	fmt.Println(removeDuplicates(nums))
}
