## aws cloudfront 
- edge location
  - 전세계 지역마다 설치되어 있는 컬렉션
  - 컨텐츠 정보 캐쉬에 저장 
  - origin과 대화 후 cdn 캐쉬에 저장 
  - 캐쉬는 영구적이지 않음
- 정적 동적 실시간 웹사이트 컨텐츠를 유저들에게 전달 
- 컨텐트 딜리버리 네트워크(content delivery network)
- 분산 네트워크(distributed network)

### cloudfront words 
- edge location: 컨텐츠들이 캐시에 보관되어지는 장소 
- origin: 원래 컨텐츠들이 들어있는 곳 
웹서버 호스팅이 되어지는 곳
s3, ec2 인스턴스가 오리진이 될 수 있음 
- distribution: cdn에서 사용되어지며 edge location들을 묶고 있다는 개념

### aws cloudfront practice 
- origin 생성: 원래 콘텐츠 생성(웹서버 호스팅)
#### create distribution
- delivery method:
    - web: http & https 
    - rtmp: real time message protocol
- option
  - origin domain name
  - origin path
  - restrict bucket access
    - 해당 옵션을 누르는 경우, cdn을 통해서만 접근이 가능
  - origin access identity:
      - iam과 유사
  - grant read permission on bucket
    - 버킷 읽기 허용
- default cache setting
  - cloudfront
    - put, post 에도 edge location 사용가능
  - cache and origin settings
    - ttl (time to live)
    - 얼마나 오랫동안 캐쉬에 살 수 있는지 설정 가능
    - cache policy
    - restrict viewer access
      - 특정 유저만 웹 사이트 컨텐츠 허용
    - price class
      - all edge : 비용 지불 
    - alternate domain names 
    - ssl certificates
      - 개인 ssl을 원하면 aws 인증서에서 가져올 수 있음
      - iam을 통하여 인증서를 저장하고 불러오기 가능
    -  http version
    -  geo restriction