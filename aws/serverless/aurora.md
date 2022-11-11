어떻게 db는 aws lambda 같이 많은 커넥션들을 맺을 수 있을까?
- data api [요 방법]
- rds proxy
  - 지속적인 연결 대신 api를 통해 접근
  - api 형식으로 호출
  - secret manager 
    - 보안 정보를 보호하는데 도움