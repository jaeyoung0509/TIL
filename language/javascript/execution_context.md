### 실행 컨텍스트 

실행 가능한 코드
- 전역 (리터럴은 실행가능하지 않음!)
- 함수 
- eval
- module (코드 뭉치)

#### call stack
[link](https://www.youtube.com/watch?v=pfQfEwnJHRs&list=PLEOnZ6GeucBW11uFNvzxToKym9Zv74hxh&index=11)
- lexical : 사람이 이해하는 순서대로
```
global execution context 
```

global lexical environment
```
- env record 
  - object env.rec 
  - declarative env.rec
- outer lex environment
```