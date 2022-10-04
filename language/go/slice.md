![](static/image.png.png)
![](static/2022-10-04-16-48-10.png)

- golang sentinel value

- empty vs nil slice 
slice and maps encoding differently in json when nil

``` golang
func main() {
    var a []int
    j1 , _ := json.Marshal(a)
    // then j1 is null

    b := []int{}
    j2 ,_ := json.Marshal(b)
    // then j2 is []
}
```

cf) 
```go
if a == nil{
    //anti pattern
}

if len(a) == 0 {
    // good pattern
}
```

```golang
v := make([] int , 0 , 5)
// but result is []int{}
```
### how slice works 
```go
func main() {
    a:= [3]int{1,2,3} // 1 2 3
    b := a[:1]  // 1 
    // b's len is 1 but capacity is 3
    c := b[0:2] // 1 2 ???????
}
```
### slice instance expression
```go
a:= [3]int{1,2,3}
 d:= a[0:1:1]
```
- `[i:j:k]`
- len : i - j
- capacity: k-i
- using this expression, when slice's capacity is full, if some value is appended , make new piece of memory and copy and allocate 


> you've got two things already going on you've got slices are aliases to some
>underlying array it may have the name a it may not if i had created b all right 


