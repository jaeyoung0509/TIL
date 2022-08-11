## go generic
- 1.18에 추가
- go는 강타입언어 , 여러 타입을 지원하는 함수를 만들기 쉽지 않음 귀찮아~!! -> 여러 타입에서 동작하는 함수 만들고 싶어
- go에서는 어떤 타입은 대소 비교를 할 수 없음   
- 타입 제한자 
- - go에 미리 정의된 타입 제한자도 사용할 수 있음 
- - `interface` 키워드를 통해서 타입 제한자를 만들 수 있음
- - `~int` :  int type을 별칭으로 하는 모든 타입을 포함한다  (별칭 타입 ,하위 타임까지)
```go
// any , comparable(비교할 수 있는 == , !=)
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