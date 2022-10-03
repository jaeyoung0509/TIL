## latency
- 떨어진 두 컴퓨터 사이에는 레이턴시가 발생할 수 밖에 없음
- 100ms : 내가 어떤 응답을 보냈을때 받는 시간
- 격투게임을 한다고 생각하면 디비가 지구반대편에 있으면 (보통 60프레임)
- 주먹버튼을 눌렀을 때 주먹을 누르기 까지 오래 걸리면 ..?
- 어떻게 하면 레이턴시를 줄일 수 있을까? & 눈속임
- round trip time 왕복속도


## 연결 & 안전성
- 인터넷은 world wide web 
- 한지점에서 다른지점으로 가는게 다이렉트가 아닌 여러 경로를 걸쳐서 감
- 한국에서 아마존 
집 -> kt -> kt백본 -> 일본 백본 -> 해상케이블 -> 아마존 서버
- 실제 일본 지진 났을 때 미국서버 접속이 느려졌던 일이 있음 

## 순서 비보장 
- 전선으로 연결된건 queue라고 생각하면 됨 
1,2,3 -> 1,2,3
- 인터넷에선 순서가 보장이 안됨 
- 인터넷은 월드 와이드 웹이다 보니까 무수히 많은 경로가 존재함
- 보통 패킷을 살포해서 가장먼저 도착한 경로를 캐싱함
- 어떤 패킷은 빨리가고 다른 패킷은 늦게 올 수 있음 

### 결론
- 지연 시간
- 연결이 불안
- 순서 비보장 