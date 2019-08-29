package main

import "fmt"

func main() {
	str := []rune{'c', 'a', 'r', 'r', 'a', 'c', 'e'}
	fmt.Println(palindromable(str))
}

func palindromable(str []rune) bool {
	oddCountLetters := map[rune]int{}
	for _, i := range str {
		if _, ok := oddCountLetters[i]; ok {
			delete(oddCountLetters, i)
		} else {
			oddCountLetters[i] = 1
		}
	}
	// oddCountLetters length should be equal to 1 or 0
	return len(oddCountLetters) <= 1
}
