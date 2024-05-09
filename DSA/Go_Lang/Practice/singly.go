package main

type node struct {
	element int
	next    *node
}

type singlyLinkedList struct {
	head *node
	tail *node
	size int
}

func (l *singlyLinkedList) len() int {
	return l.size
}

func (l *singlyLinkedList) isempty() bool {
	return l.size == 0
}

func (l *singlyLinkedList) addfirst(e int) {
	new := &node{e, nil}
	if l.isempty() {
		l.head = new
		l.tail = new
	} else {
		new.next = l.head
		new = l.head
	}
	l.size++
}

func (l *singlyLinkedList) addlast(e int) {
	new := &node{e, nil}
	if l.isempty() {
		l.head = new
		l.tail = new
	} else {
		l.tail.next = new
		l.tail = new
	}
	l.size++
}

func (l *singlyLinkedList) addany(e int, position int) {
	new := &node{e, nil}
	if l.isempty() {
		l.head = new
		l.tail = new
	} else {
		p := l.head
		for i := 0; i < position-1; i++ {
			p = p.next
		}
		new.next = p.next
		p.next = new
		l.size++
	}
}
