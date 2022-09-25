javascript destructuring 
```
arr = [1 ,2 ,3]
arr2 = [1 ,2 ,3]
```

함수 표현식이 어떻게 불리냐에 따라 
function , method 
- f()  function
- new f()  생성자 함수 메소드

`this` -> 메모리 객체 인스턴스를 가르킴
es11에선 global this

### `strict mode` 
- 일반함수에서 this는 window 지칭
- hoisting strict mode에선 지향
- eslint & prettier 오해구문 소지 쓱쓱 
- built -in  
   - 표준 빌트인 
   - 호스트 빌트인(브라우저 빌트인)
     - dom : element
     - bom : browser location, history,~
   - 커스텀 빌트인

### compiler <-> interpreter
- 인터프리터는 대신에 평가가 있음 
- 스코프에 따라 `실행 컨텍스트`
- `도메인` , `스코프` , `컨텍스트`
- 컴파일 언어는 미리 타입 선정 
- 인터프리터터 언어는 위치

#### 인터프리터 평가 순서 
- 젼역코드 평가 (위치)
- 실행 -> 타입을 확보 
- 함수 실행 컨텍스트(heap)
- function object(함수 코드)
- 전역마다 메모리가 다르고 
- 함수마다 메모리 다르고 

