package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func ParseRangePair(s string) Node {
	parts := strings.Split(s, "-")

	p1, err := strconv.Atoi(parts[0])
	if err != nil {
		panic(err)
	}

	p2, err := strconv.Atoi(parts[1])
	if err != nil {
		panic(err)
	}

	return Node{
		start: p1,
		end:   p2,
	}
}

func main() {
	logfile := "./input.txt"
	f, err := os.OpenFile(logfile, os.O_RDONLY, os.ModePerm)
	if err != nil {
		log.Fatalf("open file error: %v", err)
		return
	}
	defer f.Close()

	sc := bufio.NewScanner(f)
	mode_populate_ranges := true
	list := DoublyLinkedList{}
	result := 0

	for i := 0; sc.Scan(); i++ {
		line := sc.Text() // GET the line string

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

	fmt.Printf("Result: %d\n", result)

	if err := sc.Err(); err != nil {
		log.Fatalf("scan file error: %v", err)
		return
	}

}
