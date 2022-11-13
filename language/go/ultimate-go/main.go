package main

import "fmt"

func increment1(inc int) {
	inc++
}

func increment2(inc *int) {
	*inc++
}

type A struct{}

func makeNil() interface{} {
	var a A
	return a
}

func main() {

	// count := 10

	// fmt.Println("count:\tValue Of[", count, "]\tAddr Of[", &count, "]")
	// increment1(count)

	// // increment1 를 실행한 다음의 count 값을 출력한다. 바뀐 것이 없다.
	// fmt.Println("count:\tValue Of[", count, "]\tAddr Of[", &count, "]")

	// increment2(&count)
	// fmt.Println("count:\tValue Of[", count, "]\tAddr Of[", &count, "]")

	// slice2 := make([]string, 5, 8)
	// // pointer and length of size -> 5
	// //capacity -> 8
	// slice2[0] = "Apple"
	// slice2[1] = "Orange"
	// slice2[2] = "Banana"
	// slice2[3] = "Grape"
	// slice2[4] = "Plum"

	// inspectSlice(slice2)

	// n := makeNil()
	// if n == nil {
	// 	fmt.Println("is nil")
	// } else {
	// 	fmt.Println("not nil")
	// }

	x := make([]int, 7)
	for i := 0; i < 7; i++ {
		x[i] = i * 100
	}
	twohundred := &x[1]
	fmt.Println("%d", *twohundred)

	x = append(x, 800)
	x[1]++
	fmt.Println(x[1], *twohundred)

}

func inspectSlice(slice []string) {
	for i := range slice {
		fmt.Printf("[%d]%p %s\n", i, &slice[i], slice[i])
	}
}
