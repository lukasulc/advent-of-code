package main

import (
	"fmt"
	"strconv"
	"strings"
	"testing"
)

func TestOfficialExample(t *testing.T) {

	input := []string{
		"3-5",
		"10-14",
		"16-20",
		"12-18",

		"1",
		"5",
		"8",
		"11",
		"17",
		"32",
	}

	mode_populate_ranges := true
	list := DoublyLinkedList{}
	result := 0

	for i := 0; i < len(input); i++ {
		line := input[i] // GET the line string

		// blank line: switch mode, but do not pass the blank line itself
		if strings.TrimSpace(line) == "" {
			mode_populate_ranges = false
			fmt.Printf("List populated with %d nodes out of %d ranges\n", list.length, i)
			continue
		}

		if mode_populate_ranges {
			node := ParseRangePair(line)
			list.InsertSorted(&node)
			continue
		}

		id, err := strconv.Atoi(line)
		if err != nil {
			panic(err)
		}

		curr_node := list.head
		for j := 0; j < list.length; j++ {
			if curr_node.start <= id && id <= curr_node.end {
				result += 1
				break
			}
			curr_node = curr_node.next
		}

	}
}
