package main

import "fmt"

func main() {
	// variable := map [keytype]valuetype{key:value,key:value,key:value}
	x := map[string]int{"xyz": 37, "abc": 28, "pqr": 20}
	fmt.Print(x)
	fmt.Println("\n", x["xyz"])
}
