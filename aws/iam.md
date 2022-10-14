## iam
- access key , private key
- granular permission
  - 세밀한 접근 권한 부여 기능
- 비밀번호 변경 가능
- multi factor auth 기능
  - root user는 mfa 지향
- group
- user
- role
  - 하나 & 다수의 정책 부여 가능
- policy
  - 정책은 그룹, 역할에 추가시킬 수 있음
- iam is universal
  - 지역 설정이 필요 없음

### iam simulators
- 개발환경에서 실제환경으로 빌드하기전 IAM 정책이 잘 작동되는지 테스트하기 위함
- IAM과 관련된 문제들을 디버깅하기에 최적화 된 툴 

## dynamo simulators
- 서비스 이용해서 유저 , 그룹별로 서비스별 권한 시뮬레이션 가능