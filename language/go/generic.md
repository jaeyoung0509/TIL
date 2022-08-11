## go generic
- 1.18에 추가
- go는 강타입언어
- 타입 제한자 
- - `interface` 키워드를 통해서 타입 제한자를 만들 수 있음
```go
type Integer interface {
    int | int16 | int32 | int64
}

type Float interface {
    float32 | float64
}

func min [T Integer | Float](a , b T) T {
    return a + b
}
```