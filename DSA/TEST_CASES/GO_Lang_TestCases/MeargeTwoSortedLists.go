// First  - choose the head
// Second - choose the node with less Val, append it to the new list being built and
// move the corresponding pointer one step further, e.g. list1 = list1.Next.
// Third - in the end of the cycle you have reached the end of one of the given lists,
// so what is left is to append the remaining tail to the resulting merged list.

package main

import "fmt"

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 []int, list2 []int) {
	if list1 == nil {
		return list2
	}

	if list2 == nil {
		return list1
	}

	var head *ListNode
	if list1.Val < list2.Val {
		head = list1
		list1 = list1.Next
	} else {
		head = list2
		list2 = list2.Next
	}

	dummy := head
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			dummy.Next = list1

			list1 = list1.Next
		} else {
			dummy.Next = list2

			list2 = list2.Next
		}
		dummy = dummy.Next
	}

	if list1 == nil {
		dummy.Next = list2
	}

	if list2 == nil {
		dummy.Next = list1
	}

	return head
}

func main() {
	list1 := []int{1, 23, 423, 458}
	list2 := []int{3, 5, 423, 2222}
	A := &mergeTwoLists(list1, list2)
	fmt.Println(A)

}
