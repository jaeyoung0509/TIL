python asyncio 역사 
https://minzoovv.dev/python/history-of-asyncio/


### 이벤트 루프
- 모든 비동기 응용 프로그램의 핵심
- 이벤트 루프는 비동기 태스크 및 콜백을 실행하고 네트워크 io 연산 수행 
자식 프로세스 수행
- 이벤트 루프는 스레드(main thread)에 실행되며 그 스레드에서 모든 콜백과 테스크를 실행

### 퓨처 객체 (future)
- 퓨처 객체는 저수준 콜백 기반의 코드와 고수준 async / await 코드 간에 다리를 놓는데 사용
- 여기서 다리는 asyncio 트랜스포트를 사용하며 구현된 프로토콜에서 고수준 async / await 코드와 상호 운용
- 사용자가 만나는 api에서 future 객체를 절대 노출하지 않으며 , future 객체를 만드는 권장 방법은 loop.create_future()를 호출 
- 이런식으로 대체 이벤트 루프 구현이 자신의 최적화된 future 객체 구현을 주입

## 저수준
### 트랜스포트와 프로토콜
- 저수준 이벤트 루프 api에서 사용 
- 콜백 기반 프로그래밍 스타일 사용
- 최상위 수준에서 트랜스포트는 어떻게(`how`)바이트를 전송할지를 다루지만,
프로토콜은 어떤(which) 바이트를 전송할지를 결정
- 트랜스포트 객체와 프로토콜 객체 간에는 항상 1:1 관계
#### 트랜스포트
- 다양한 종류의 통신 채널을 추상화하기 위해 제공
- 항상 asyncio 이벤트 루프에 의해 인스턴스가 생성
- tcp,udp.ssl 및 서브 프로세스 파이프를 위한 트랜스포트 구현
- 트랜스포트 클래스는 스레드 안전하지 않음(?) 
  - TODO (https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-multithreading)
#### 프로토콜 
- 사용해야 하는 추상 베이스 클래스 집합 제공 


### 정책  (policy)


## 고수준
### runners 

### coroutines and tasks
#### coroutines

#### tasks
- 코루틴을 동시에 예약하는데 사용됨

#### future
- 비동기 연산의 최종 결과를 나타내는 특별한 저수준 awaitable object
- 콜백 기반 코드를 async/await와 함께 사용하려면 asyncio의 Future 객체가 필요

#### awaitable
- there are three awaitable objects 
  - coroutines
  - tasks
  - future 
  
### stream
- 네트워크 연결로 작업하기 위해,  async await에서 사용할 수 있는 고수준 프리미티브




----
### python asyncio concept 
https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-1

#### doing things one at a time, but out of order 
- traditionally computers have been machines that do one thing at a time
- modern computers can often do multiple things at once (because of cpu cores)

#### asyncio is not one of these
- it's not about using multiple cores , it's about using a single core more efficient way

#### subroutines vs corutines
- TODO

#### stacks and frames 
- TODO

#### event loops , tasks, corutines


---
### multiple entry point
- await -> 일시정지가 될 수 있다
### frame 객체
- 함수가 실행될 떄 필요한 정보들을 가지고 있음
- used on executing a function
- contains information for executing a function
  - call stack
  - value stack
  - local variables

- corutines
  - based on generator
  - contains a frame object like thread state
    - the frame memories which index of bytecode is executed
    - the frame stores local variables
#### f.locals
- 로컬 변수
#### f.back
- 자신을 호출한 프레임(previous stack frame , this frame's caller)
- 자신을 실행한 프레임을 가르킴
- thread state  (콜 스택)
#### f.lasti
- dis를 통해 byte 코드를 볼 수 있음
- 함수가 가장 최근에 실행한 바이트 코드 
- 가장 최근의 실행한 바이트코드의 인덱스 (index of last attempted instruction in bytecode)
#### f_code
- f_code == __fcode__
- 바이트코드의 이해
 
 #### yield from 
- 제너레이터에서 또다른 제너레이터를 사용하기 위함(sub generator)
- corutines -> yield from을 
- generator와 비슷함
- await -> yield from 서브제너레이터를 실행하는것과 유사
  - 안쪽에서 yield

### event loop
- 비선점 (for non preemptive multitasking)
- 비선점 <-> 선점(스레드)
  - 선점은 언제 스위칭이 될지 알 수 없음
  - 비선점은 언제 스위칭되는지 명시적으로 
cf) 스케쥴링이란?
- 다중 프로그래밍을 가능하게 하는 동작 기법.
- 운영체제는 프로세스들에게 cpu등 지원 배정을 적절히 함으로서 시스템 성능 개선 가능
#### 순서
- task 객체 생성
  - `task._step`
  event loop call_soon에 의해 스케쥴링
  result = corutine.send(None)

#### selector
- 운영체제 풀링 객체를 매핑하기 위함
cf) 풀링이란
Pooling 기법이란 미리 데이터베이스 Connection을 여러 개 만들어서 특정 공간에 저장해 놓고, 여러 사용자가 필요할 때 마다 하나씩 꺼내서 사용하고 다시 집어 넣는 방식을 말합 


---
### cancellation
- corutine이 외부 요인에 의해 중단되었음을 알려주는 역할
- 모든 await 구문에서 발생할 수 있음
- await가 없는 코드는 아무리 길고 오래걸려도 cancel 불가능
- task 또는 future에 대한 참조를 가진 쪽에서 cancel()메소드를 부름으로서 발생