## protocol
- 약속
- 통신을 하기 위해선 약속이 필요함 
- 모스부호도 하나의 종류
- `tcp` , `udp`  
- ip -> gateway -> 하위 컴퓨터 
- port(`항구`) 
- 데이터 바이너리 (`byte`) 전기적 신호의 연속

### tcp 
-  지연시간 
-  연결 
-  - 3 way hand shake 
- 송수신 간  수신자가 송신자의 연결을 ok 답장하면 답장 메시지가 잘 갔는지 알 수 있을까?
A ->(connect request) - B
B ->(OK) ->  A
A -> (잘 받앗다) ->  B
- 이런 `3 way hand shake` 방식을 통해 연결 유무를 알 수 있음
- 패킷이 4개가 왔는데 (tcp header에 숫자)

### udp 
- 그 딴거 없다 그만큼 빠르다
- 근데 http3 quic은 다르다 !
- 유실률은 7% 정도밖에 안됨
- 그래서 게임쪽에서는  `udp`를 쓰고 싶다
- 하지만 순서보장, 연결유무, 유실 
그래서 만든게 
`reliable udp`를 만듬
- tcp는 하드웨어적으로 처리 , 위 reliable udp는 소프트웨어적으로 
- 역시 근데 만들기 진짜 어려움

