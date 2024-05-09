// Definition for singly-linked list.
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func middleNode(head *ListNode) *ListNode {
	toratile := head
	hare := head
	for hare != nil && hare.Next != nil {
		toratile = toratile.Next
		hare = hare.Next.Next
	}
	return toratile

}

func main() {

	A := []int{1, 2, 3, 4, 5}
	// middleNode(A)
	fmt.Println(middleNode(A))
}
