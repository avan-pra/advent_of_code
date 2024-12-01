package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

// Abs returns the absolute value of x.
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func amountOfOccurences(arr []int, n int) (value int) {
	value = 0

	for _, v := range arr {
		if v == n {
			value += 1
		}
	}
	return value
}

func main() {
	var s = make([][]int, 2)
	// s[0] = make([]int, 0)
	// s[1] = make([]int, )

	fd, err := os.Open("input")
	if err != nil {
		print(err)
	}
	defer fd.Close()
	rd := bufio.NewReader(fd)
	line, err := rd.ReadString('\n')

	for err == nil {
		re, _ := regexp.Compile("[0-9]+")
		ret := re.FindAllString(line, -1)
		left, _ := strconv.Atoi(ret[0])
		right, _ := strconv.Atoi(ret[1])
		s[0] = append(s[0], left)
		s[1] = append(s[1], right)

		line, err = rd.ReadString('\n')
	}

	total := 0
	for i := range s[0] {
		total += s[0][i] * amountOfOccurences(s[1], s[0][i])
	}

	fmt.Println(total)
}
