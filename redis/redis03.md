# redis study

[https://www.youtube.com/watch?v=mPB2CZiAkKM](https://www.youtube.com/watch?v=mPB2CZiAkKM)

[https://www.youtube.com/watch?v=QEKDpToureQ](https://www.youtube.com/watch?v=QEKDpToureQ)

[https://developer.redis.com/develop/python/fastapi/](https://developer.redis.com/develop/python/fastapi/)

## 레디스

- in-memory
- bsd license
- only 1 commiter
    - 레디스는 딱 한명밖에 없음

### 캐쉬

- dynamic programming

![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled.png)

- db도 내부적으로 캐쉬갖고 있음
    - 파레토 법칙(2:8) 
    전체 요청의 80%는 20%의 사용자
    - 성능은 좋지 않음
- cache #1  look aside cache

![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%201.png)

- write back
    - 데이터 유실 가능성
    - 배치작업 시

![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%202.png)

### 왜 collection이 중요한가?

- 개발의 편의성
- 개발의 난이도
- `memcache` 와 차이점
    - 레디스는 여러 자료구조를 제공 (비지니스 로직에만 신경쓸 수 있음)
    - 랭킹기능을 구현한다면? → redis sorted set을 사용하면 쉽게 구현가능
    - 친구 리스트, key - value
        - 두개의 독립적인 작업인데  (acid)  타이밍이 겹친다면?
        
        ![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%203.png)
        
        ![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%204.png)
        
    - redis의 자료구조는 atomic하기 때문에 race condition을 피할 수 있음
        - 그래도 잘못짜면 발생
        

### 사용 처

- remote data store
    - 여러 서버에서 데이터 공유할 때
- atomic 보장이 필요한 것들
    - 친구 리스트
- 주로 많이 쓰는 곳들
    - 인증 토큰
    - ranking
    - 유저 api limit
    - api limit
    - job queue

### collections

- strings  : key value
    - prefix를 붙힐때 어떻게 붙히는게 좋을까?
    - key를 잘 잡는것도 중요하다
- list
    - lpush, lpop
    - rpush, rpop
    - job queue에 많이 사용
    - 명령어 선택에 주의하자 (시간 복잡도가 다름)
- set
    - 데이터가 있는지 없는지 체크하는 용도
    - 팔로우,친구목록 `유니크 한 값` 에 자주 쓰임
- sorted_set
    - 랭킹에 따라서 순서가 바뀌길 바란다면
    - sorted set의 score는 정수가 아님
- hash
    - key 밑에 sub key - value
- 하나의 컬렉션에 너무 많은 아이템을 담으면 좋지 않음
    - 10000개 이하
- expire는 collection의 item 개별을 걸 수 없음 , collection 전체에 대해 걸림

## redis 운영

- 메모리 관리를 잘하자
- o(n)명령어 주의
- replication
- 관련 설정 tip

### 메모리 관리

- in-memory
- physical memory 이상을 사용하면 문제가 발생
    - swap이 있다면 해당 메모리 page 접근시 마다 늦어짐
    - max memory를 설정하더라도 이보다 더 사용할 가능성이 큼
        - jemalloc을 씀에도 불구하고 redis는 자기가 사용하는 메모리가 얼마인지 모름
        - memory
    - rss 값을 모니터링 해야 함
- 큰 메모리를 사용하는 instance 하나보다는 적은 메모리를 사용하는 instance가 안전

![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%205.png)

- write가 heavy한 경우에는 메모리를 2배까지 사용할 수 있음
- 메모리 파편화가 발생할 수 있음

### o(n)명령어 주의

- redis는 싱글 스레드
- 레디스가 동시에 여러개의 명령을 처리할 수 있을까?

![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%206.png)

- 한번에 하나의 명령만 수행 가능
    - 그럼 긴 명령어는 어떻게 해?  `지양`
- 대표적인 o(n) 명령
    - keys
        - 대신 scan 명령어 사용!
    - flushall , flushdb
    - delete collections
    - get all collections
        - 일부만 가져온다거나, 큰 컬렉션을 여러개의 컬렉션으로 나눠서
    
    ## redis replication
    
    - async replication
        - replication log 발생 가능성
    - dbms로 보면 statement replication과 유사
        - db에서 now를 예시로 들면 primary 와 secondary에서 값이 다를 수 있음
    
    ![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%207.png)
    
- replication과정에서 fork가 발생하므로 메모리 부족이 발생할 수 있음

![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%208.png)

- 레플리카의 경우에만 rdb/aof 설정

### 데이터 분산 방법

- apllication
    - consistent hashing
        - 자기보다 크고 제일 가까운 hash 값
        - key의 hash가 일정하면 리벨런싱이 일어나도 데이터의 변동이 적음
    - modular 와 id 로 분산
        - 서버증가 할때마다 리벨러싱이 일어나는데
            - 50%이상이면? → 장애에 취약
    - sharding
        - 상황마다 다름
        - range
        - indexed
            - 해당 키가 어디에 저장되어야 할 관리가 서버가 따로 존재
            - 인덱스 서버가 죽으면 장애 발생
- redis cluster
    - 해쉬 기반으로 구분
    - 장점
        - 자체적인 failover
        - slot 단위의 데이터 관리
    - 단점
        - 메모리 사용량이 더 많음
        - library 구현이 필요
    
    ![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%209.png)
    
    ### redis failoveer
    
    - cordinator
        - zookeeper , etcd, consul 등의 coordinator 사용
    - vip/dns
        - 가상 ip를 할당
        - 클라이언트에 추가적인 구현 필요 x
        - dns기반은 dns cache ttl 관리 필요

![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%2010.png)

---

## AWS

- Elastic Cache: 메인 데이터베이스의 워크로드를 분산하고 캐싱 기능으로 활용
- Amazon MemoryDB for redis: 메모리 데이터베이스로 메인 데이터베이스 자체로 사용을 상정
    - 최근 출시
    - 내구성이 떨어지는것을 보완
    - 타임시리즈 디비, IOT 기기들의 메인디비
    - [https://aws.amazon.com/ko/memorydb/features/](https://aws.amazon.com/ko/memorydb/features/)

### elastic cache

- [https://www.youtube.com/watch?v=WcE5G4QQ_zY](https://www.youtube.com/watch?v=WcE5G4QQ_zY)

![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%2011.png)

- read cache
    - 많이 변하는 데이터의 경우에는 성능향상을 가져올 수 없음
- 레디스를 자체적으로 관리하는것은 어려움
    - db cpu 증가
    - latency 증가
    - ratelimit도 안됨
    - 주요 원인
        - 하드웨어 문제
        - out of memory (스냅샷을 뜨기위해 메모리 50% 여유가 필요)
    
    → elastic cache 도입
    
    ![Untitled](redis%20study%20f657f409fc1744499476a5f58410838b/Untitled%2012.png)