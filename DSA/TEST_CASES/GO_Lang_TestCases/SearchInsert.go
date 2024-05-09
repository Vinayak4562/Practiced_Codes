package main

import "fmt"

func searchInsert(nums []int, target int) int {
	if nums[len(nums)-1] < target {
		return len(nums)
	}
	for i := 0; i < len(nums); i++ {
		if nums[i] == target {
			return i
		}
		if nums[i] > target {
			return i
		}
	}
	return -1
}

func main() {
	L := []int{1, 2, 4, 5, 7, 8}
	// there are 6 elements in an list (0-5)

	fmt.Println(searchInsert(L, 3))
	fmt.Println(searchInsert(L, 4))
	fmt.Println(searchInsert(L, 5))
	fmt.Println(searchInsert(L, 33))
}
