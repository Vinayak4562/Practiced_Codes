package main

import "fmt"

type Node struct {
	element int
	next    *Node
	Prev    *Node
}

type dCir struct {
	head *Node
	tail *Node
	size int
}

func (c *dCir) len() int {
	return c.size
}

func (c *dCir) isempty() bool {
	return c.size == 0
}

func (c *dCir) addfirst(e int) {
	new := &Node{e, nil, nil}
	if c.isempty() {
		c.head = new
		c.tail = new

	} else {
		new.Prev = c.tail
		c.tail.next = new
		c.head.Prev = new
		new.next = c.head
		c.head = new
	}
	c.size++

}

func (c *dCir) addany(e, pos int) {
	new := &Node{e, nil, nil}
	if c.isempty() {
		c.head = new
		c.tail = new
	} else {
		p := c.head
		for i := 1; i < pos-1; i++ {
			p = p.next
		}
		new.next = p.next
		p.next.Prev = new
		p.next = new
		new.Prev = p
	}
	c.size++
}

func (c *dCir) remvany(pos int) {
	if c.isempty() {
		fmt.Println("List is empty")
		return
	} else {
		p := c.head
		i := 1
		for i < pos-1 {
			p = p.next
			i++
		}
		e := p.next.element
		p.next = p.next.next
		p.next.next.Prev = p
		fmt.Println(e)
	}
	c.size--

}

func (c *dCir) display() {
	p := c.head
	i := 0
	for i < c.len() {
		fmt.Print(p.element, "-->")
		p = p.next
		i++

	}
	fmt.Println()
}

func (c *dCir) displayprev() {
	p := c.tail
	i := 0
	for i < c.len() {
		fmt.Print(p.element, "<--")
		p = p.Prev
		i++
	}
	fmt.Println()
}

func main() {
	c := &dCir{}
	c.addfirst(11)
	c.addfirst(12)
	c.addfirst(13)
	c.addfirst(14)
	c.addfirst(15)
	c.display()
	c.displayprev()
	c.addany(111, 3)
	c.display()
	c.displayprev()
	c.remvany(3)
	c.display()
	c.displayprev()
}
