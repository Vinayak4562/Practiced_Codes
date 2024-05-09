package main

import "fmt"

func search(nums []int, target int) int {
	start, end := 0, len(nums)-1

	for start <= end {

		mid := (end + start) / 2

		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			end = mid - 1
		} else if nums[mid] < target {
			start = mid + 1
		}

	}
	return -1
}

func main() {
	nums := []int{-1, 2, 6, 8, 9}
	fmt.Println(search(nums, -1))
	fmt.Println(search(nums, 1))
	fmt.Println(search(nums, 2))
	fmt.Println(search(nums, 8))
	fmt.Println(search(nums, 10))
}
