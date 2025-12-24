package main

import (
	"log"
)

type Node struct {
	prev  *Node
	next  *Node
	start int
	end   int
}

type DoublyLinkedList struct {
	head   *Node
	tail   *Node
	length int
}

func (list *DoublyLinkedList) AppendBeginning(n *Node) {
	if list.head == nil {
		list.head = n
		list.tail = n
		n.next = nil
		n.prev = nil
	} else {
		n.prev = nil
		n.next = list.head
		list.head.prev = n
		list.head = n
	}
	list.length++
}

func (list *DoublyLinkedList) AppendEnd(n *Node) {
	if list.head == nil {
		list.AppendBeginning(n)
	} else {
		n.next = nil
		n.prev = list.tail
		list.tail.next = n
		list.tail = n
	}
	list.length++
}

// func (list *DoublyLinkedList) Insert(n *Node, idx int) {
//     if idx >= list.length || idx <= 0 {
//         fmt.Printf("Index out of range!")
//     } else {
//         curr_node := list.head
//         for i := 0; i < idx; i++ {
//             curr_node = curr_node.next
//         }
//         n.prev = curr_node
//         n.next = curr_node.next
//         curr_node.next = n
//         n.next.prev = n
//         list.length++
//     }
// }

func (list *DoublyLinkedList) InsertSorted(n *Node) {
	if list.head == nil {
		list.AppendBeginning(n)
		return
	}

	curr_node := list.head
	for i := 0; i < list.length; i++ {
		if curr_node == nil {
			log.Printf("ADD: New node (%d-%d) is after tail", n.start, n.end)
			list.AppendEnd(n)
			return
		}

		// The new range is contained in the old range, skip adding the new node
		if curr_node.start < n.start && curr_node.end > n.end {
			log.Printf("SKIP: New node (%d-%d) is inside (%d-%d)", n.start, n.end, curr_node.start, curr_node.end)
			return
		}

		// New node has ranges which don't overlap and are bigger then current node,
		// continue to next node.
		if curr_node.end < n.start {
			log.Printf("CONTINUE: New node (%d-%d) is after (%d-%d)", n.start, n.end, curr_node.start, curr_node.end)
			curr_node = curr_node.next
			continue
		}

		// New node has ranges which don't overlap and are smaller then current node.
		// Since it's also bigger then previous it should be added before current.
		if curr_node.start > n.end {

			if curr_node.prev == nil {
				log.Printf("ADD: New node (%d-%d) is before head (%d-%d)",
					n.start, n.end, curr_node.start, curr_node.end)
				list.AppendBeginning(n)
				return
			}

			log.Printf("ADD: New node (%d-%d) is between (%d-%d) and (%d-%d)",
				n.start, n.end, curr_node.start, curr_node.end, curr_node.prev.start, curr_node.prev.end)
			n.next = curr_node
			n.prev = curr_node.prev
			curr_node.prev.next = n
			curr_node.prev = n
			list.length++
			return
		}

		// I need to expand only to the right as I already checked that new node
		// is not going to be smaller then current node.
		// Also, make sure to remove nodes as they are swallowed by the new node.

		// Expand on the left
		if curr_node.start > n.start {
			tmp_node := curr_node.prev

			for j := 0; tmp_node != nil; j++ {
				// New Node didn't enter the previous range, end expanding
				if tmp_node.end < n.start {
					curr_node.start = n.start
					break
				}

				// New node ended up in the middle of the one of the previous ranges
				if tmp_node.start <= n.start /* && n.start <= tmp_node.end | implicit */ {
					curr_node.start = tmp_node.start
					curr_node.prev = tmp_node.prev

					log.Printf("CHECK: New node (%d-%d) is overlapping with (%d-%d), removing it",
						n.start, n.end, tmp_node.start, tmp_node.end)
					list.length -= j + 1
					break
				}

				// New node swallows previous range
				log.Printf("REMOVE: New node (%d-%d) is swallowd (%d-%d), removing it",
					n.start, n.end, tmp_node.start, tmp_node.end)

				// if tmp_node.start > n.start | implicit
				curr_node.prev = tmp_node.prev
				tmp_node = curr_node.prev
				tmp_node.next = curr_node
				list.length--
			}
		}

		// Expand on the right
		if curr_node.end < n.end {
			tmp_node := curr_node.next

			for j := 0; tmp_node != nil; j++ {
				// New Node didn't enter the next range, end expanding
				if tmp_node.start > n.end {
					curr_node.end = n.end
					break
				}

				// New node ended up in the middle of the one of the previous ranges
				if /* tmp_node.start <= n.end && | implicit && */ n.end <= tmp_node.end {
					curr_node.end = tmp_node.end
					curr_node.next = tmp_node.next

					log.Printf("REMOVE: New node (%d-%d) is overlapping with (%d-%d), removing it",
						n.start, n.end, tmp_node.start, tmp_node.end)
					list.length -= j + 1
					break
				}

				// New node swallows previous range
				log.Printf("REMOVE: New node (%d-%d) is swallowd (%d-%d), removing it",
					n.start, n.end, tmp_node.start, tmp_node.end)

				// if tmp_node.end < n.end | implicit
				curr_node.next = tmp_node.next
				tmp_node = curr_node.next
				tmp_node.prev = curr_node
				list.length--

			}
		}
		return
	}
	// n.prev = curr_node
	// n.next = curr_node.next
	// curr_node.next = n
	// n.next.prev = n
	// list.length++
	log.Printf("ADD: New node (%d-%d) is after tail", n.start, n.end)
	list.AppendEnd(n)
}
