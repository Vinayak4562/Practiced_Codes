package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5, 6}
	fmt.Println(a)
	b := a[1:3] // start value is inclusive & end value is exlusive so it will disply only index val 1 and 2.
	fmt.Println(b)
	b1 := a[:3] // start value is inclusive & end value is exlusive so it will disply only index val 0,1 and 2.
	fmt.Println(b1)
	b2 := a[3:] // start value is inclusive & there is no end value so it will disply only index val 3,4,5.
	fmt.Println(b2)
	b3 := a[:] // there is no start and no end values so it will disply all index values.
	fmt.Println(b3)
	b4 := a[1] // start value is inclusive & there is no end value so it will disply only index val 1
	fmt.Println(b4)
	b5 := append(a[:], 111) // it will append at the end of the arry.
	fmt.Println(b5)
	b6 := append(a[:2], 111) // it will append at the second index of the arry.
	fmt.Println(b6)
}
