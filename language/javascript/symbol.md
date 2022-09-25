#### symbol
- 중복되지 않는 값 
- 엔진 어딘가에 static 으로
- Enum과 Iterator 역할 
- 동시에 여러개 숫자를 세는 경우
- function은 비동기
```javascript
sb = Symbol("sb")
sb2= Symbol("sb2")
```
- enum + iterable

#### symbol1 (enum)

#### symbol2 (iterator)

--- 
- get nextSeq() -> sync 
- AOP 어떤 함수를 부르기전에 통과해야 됨 (미들웨어)
- call 하는 순간 queue에 넣어주기
- pop하는 순간 callback
- 동시 호출을 막음
---
### spread , destructuring
```javascript
func sum () {
   ...arguments.reduce()
}
```
- 외부 값을 바꾸면 안됨 (`...`destructuring 사용하기)
#### 권장 표현 
```javascript
sum(...args) 
```