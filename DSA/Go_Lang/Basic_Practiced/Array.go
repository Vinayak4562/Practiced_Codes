package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5, 6}
	fmt.Println(a)
	// a1 := [3]int{1, 2, 3, 4, 5, 6} it will through an error index is out of bonds
	a1 := [3]int{1, 2, 3}
	fmt.Println(a1)
	a2 := [2][3]int{{1, 2, 3}, {4, 5, 6}}
	fmt.Println(a2)

	a3 := [3][3]int{{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9}}
	fmt.Println(a3)

	s := []string{"vinayak", "vishal", "ramesh", "moin", "nandu", "suhas"}
	fmt.Println(s)
	s = append(s, "Meghu")
	fmt.Println(s)

	// s1 := [3]string{"vinayak", "vishal", "ramesh", "moin", "nandu", "suhas"} it will through an error index is out of bonds
	s1 := [3]string{"vinayak", "vishal", "ramesh"}
	fmt.Println(s1)

	s2 := [][]string{{"vinayak", "vishal", "ramesh"}, {"moin", "nandu", "suhas"}}
	fmt.Println(s2)

}
