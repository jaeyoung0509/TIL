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