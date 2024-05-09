package main

import "fmt"

func twoSum(nums []int, target int) []int {
	for i, right := range nums {
		for j, left := range nums {
			if right+left == target && i != j {
				return []int{i, j}
			}
		}
	}
	return nil
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6}
	TS := twoSum(nums, 9)
	fmt.Println(TS)

}
