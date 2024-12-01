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

func getMin(arr []int) (value int, index int) {
	value = int(0xffffffff)
	index = 0

	for i, v := range arr {
		if value > v {
			value = v
			index = i
		}
	}
	return value, index
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
	for len(s[0]) != 0 {
		value1, index1 := getMin(s[0])
		value2, index2 := getMin(s[1])

		total += Abs(value1 - value2)

		s[0] = append(s[0][:index1], s[0][index1+1:]...)
		s[1] = append(s[1][:index2], s[1][index2+1:]...)
	}

	fmt.Println(total)
}
