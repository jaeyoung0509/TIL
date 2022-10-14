### ec2
- elastic compute cloud
- 크기가 유연하게 변경가능
  - 예측하기 어려운 데이터 사용량

### 다양한 지불방법
- on-demand : 시간당 가격이 고정
  - 개발 초기단계
- reserved: 한정된 ec2 용량 사용 가능
  - 기차로 치면 지정석 느낌
  - 조금 더 저렴하게 사용가능 
  - on-demand와 다르게 크기를 늘리고 줄일 수 없음
  - 안정된, 예상 가능한 workload시 reserved 사용 권장 
  - 선불로 인한 컴퓨팅 비용 대폭 감소 
- spot: 가격을 경매로 구매 가능
  - 인스턴스의 시작 / 끝시점에 구애받지 않을 경우 권장


### ebs
- elastic block storage 
- 디스크 볼륨 위에 file system이 생성
- ebs는 특정 availability zone에 생성

#### az
- availability zone 하나의 리전안에 여러 az존재 가능 
- 복제본 , disaster recovery
- ec2와 특정서비스 사용시 , az 설정 필요

#### ebs 볼륨 타입
- ssd
- hdd

### elb
- elastic load balancer
- 수많은 서버의 흐름을 균형있게 흘러보내는 역할
- 하나의 서버로 traffic이 물리는 병목현상 방지
- traffic의 흐름을 unhealthy -> healthy instance
-  three elb type 
#### application load balancer
- osi layer 7에서 작동
- http, https와 같은 traffic의 load balancer에 가장 적합 
- 고급 request 라우팅 설정을 통하여 특정 서버로 request (루트 변경 가능)
#### network load balancer
- osi layer4 
매우 빠른속도를 자랑 
- 극도의 performance 요구하는 tcp traffic에서 적합
- 초당 수백만개의 request 아주 미세한 딜레이 처리 가능
- 구글 네이버..
#### elastic load balancer
- 레거시이지만 application & network 모두 지원
#### elb error 
- 504 
- gateway time out 
- 웹서버, 데이터베이스 레이어에서 종종 
#### x-forward-for header
`public ip address` ->(dns) -> `private ip address` -> `ec2`
- ec2는 private address 밖에 볼 수 없음 
- public ip address 를 알 수 없음
  - x-forward-for 이용해 가능


#### route53
- aws에서 제공하는 dns 서비스
- usage: ec2 instance s3 bucket load balancer
  
#### vpc 
- 하나의 vpc 안에 공유된 컴퓨팅 시스템 사용 가능

#### subnet 
- TODO 