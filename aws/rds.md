## rds


### rds back up
- automated backups 
- db snapshot

### automatedㄹ저 backups
- point in time 
- retention period 안에 어떤 시간으로 돌아가게 할 수 있음 
- ab는 그날 생성된 스냅샷과 transaction logs(TL) 보관 
- 디폴트는 AB기능이 설정 백업 정보는 S3에 저장 
- AB동안 약간의 IO suspension 존재 할 수 있음

### db snapshot  
- 주로 사용자에 의해 
- 원본 rds 인스턴스 삭제해도 스냅샷은 존재

### multi az 
- multi availability zone 
- rds db에 변화가 생기면 다른 az존에 복재본이 생성 
- aws에 자동으로 관리 
- 원본 rds에 다른 문제가 생길 시 자동으로 복제
- disaster recovery only 

### read replica 
- 읽기 전용 
- 성능 향상을 위한 읽기 전용 복사본 
- read heavy
- 최대 5개의 read replica 허용

### redis vs memcached  
- 가장 단순한 캐싱 모델 ->memcached
- object caching -> memcached
- 캐시 크기 마음대로 -> memcached
- multi az -> redis 
- list, set -> redis
- sorting -> redis 