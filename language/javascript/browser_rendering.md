### dom
- feat html , http
- browser rendering 
  - 밑그림
  - 메모리에 `dom tree`
  - https
  - index.html
  - 
- browser paging 
  - 색칠하기

- 크롬이 속도를 올릴 수 있었던 방법 
  - 동시에 요청하기
  - connection을 여러개로
  - 병렬로 
  - 브라우저 요청이 계속 큐에 쌓이는것은 지양
  - 요청마다 컨넥션이 다 그래서 다 다름
  - contentLength 헤더에 먼저 쏨

- 예전 브라우저는
  - pooling을 이용해
  - keep alive 
  - keep alive = true  
  - 연결을 끊지않고 계속 -> 속도는 개선 
  - 근데 동시 접속 문제가 
- nginx ,c 
  - process 기반
- java 
  - thread 기반
- node 기반  non block io
  - process 기반


- cascading 
```
css
js
```
    - css , image 
    - 데이터를 스트림으로 주면 더 빠름

- dom 추가하기
  - [link1](https://www.youtube.com/watch?v=R4lSqMa0bUk&list=PLEOnZ6GeucBW11uFNvzxToKym9Zv74hxh&index=23)
  - [link2](https://www.youtube.com/watch?v=5TGGgHDv6GE&list=PLEOnZ6GeucBW11uFNvzxToKym9Zv74hxh&index=24)