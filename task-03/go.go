package main

import "fmt"

func main() {
	n := 10

	for i := 1; i < n; i++ {
		factors := 1

		for j := 2; j <= i; j++ {
			if i%j == 0 {
				factors++
			}
		}

		if factors == 2 {
			fmt.Printf("%d is a prime number\n", i)
		}
	}
}