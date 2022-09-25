### 함수
- 함수는 한 가지 일
- 함수 리터럴 (변수에 함수 리터럴 할당)
- 객체 타입 
- es6 화살표 함수 
- string ->code : function 생성자 함수 
  
리터럴이란 
- var a = 1 표현식 & 선언문
- 1은 리터럴
- a는 식별자
- var는 키워드
```
const f = function (){
}
```
- function~ 은 함수 리터럴
- 선언문은 hoisting되면서 위로 올라감

함수는 선언문으로 정의한 함수와 함수 표현식으로 정의한 함수의 생성 시점이 다름
- 인스턴스(메모리에 잡힌다)

- 자바스크립트는 평가의 우선순위는 위에서 아래로 잡힌다 (렉시컬)
- 함수형 프로그래밍의 철학 (티키타카)

- hoisting
  - let & var 
  - var는 함수 , let은 블럭 
  - 둘이 스코프가 다름

- 실행 context (해쉬맵)
```
last |  a 
_    |  &100
```

- 함수는 heap, 실행하고 나면 gc가 쓱 없애줌 
- gc가 돌고 난 후에 접근할 수 있는게 클로저?
- let은 hoisting 되는데 스코프가 다름 

- reflection?
  - 실행하기 전까지는 그저 문자
  - 실행하고 나면 객체 
  - 객체 속의 function을 찾아 나서는게 reflection

- 실행 context engine

원시타입은 immutable 

### hoisting
- 변수 hoisting
- 함수 hoisting
  - 함수 선언문
  - 함수 표현식 
  
함수형 언어는 평가와 실행
- 평가가 메모리 알 수 잇지
- 평가 시간에 선언된 것들을 먼저 위로 올려줌 
- const 경우엔 미리 값도 넣어 static
- 책에 따라 static , cache 혼용 