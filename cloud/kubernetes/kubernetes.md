## 쿠버네티스란 무엇인가? 
- 컨테이너 오케스트레이션 
- soa 
- 쿠버네티스를 이용해서 무엇울 해결하고자 하는것인가?
- - 높은 가용성
- - 확장성
- - disaster recovery
- 쿠버네티스는 많은 구성요소가 있음

### 구성요소 
#### pod
- kubernetes wants to abstract away the container runtime or containe
- abstraction over container 
-  pod is usually meant to run one application container inside of it you can run multiple containers 
-  usually 1 application per pod 
-   each pod gets its own IP address not the container
#### service 
- permanent ip address
- lifecycle of pod and service not connected 
#### ingress 
-  클러스터 내의 서비스에 대한 외부 접근을 관리하는 API 오브젝트

#### config map
- pods communicate each other 
- external configuration of your application
- don't put credentials into configmap 
#### secret 
- used to store secret data 
- base64 encoded 
- passwords certificates things that you don't want other people to have access

### 정리
- pod 
- service
- ingress 
- config map 
- secret 

### data storage 
- how it works in kubernetes
-  application uses and it has some data regenerate some data with this setup and data would be gone 
 #### volume 
- it basically attaches a phisycal storgaes on a hard drive to your pod 
- sotrgae on local machine
or remote , outside of the k8s cluster  
#### k8s cluster 
- cluster explicitly doesn't manage any data persistence 

#### replicate every thing 
- service has 2 functionalities
- - permanent ip 
- - load balancer
- blueprint 
- you can deployments 
- database has state 
- - need to access same 

### 쿠버네티스 동작원리 
- 동작과정 flow 
- - 컨테이너를 만들어서 저장소(hub)에 저장 
- - yaml , cli를 통해  kubectl 명령어를 통해 마스터(control-plane)에게 전달
- - 쿠버네티스 관련 명령어 요청을 받음
- - 컨테이너로 실행 (pod 단위로 관리)
#### 쿠버네티스 컴포넌트 
- 마스터 컴포넌트
- api: 
- - 스케쥴러에게 어떤 노드를 선택해야 될지 전달 후 해당 값을 기반으로 kublet에 전달
- etcd : key - value 타입의 저장소 
- - 워커노드들에 대한 상태정보 
- - 도커 컨테이너 동작중인 상태 
- - kublet 데몬을 통해(모니터링 프로그램이 포함되어 있음)
- - 위 정보들을 etcd에 저장 
- kube-apiserver: k8s api를 사용하도록 요청을 받고 유효한지 검사 
- 애드온: 모니터링 (pod /deployments)
- - 컨테이너 로그 , k8s , 운영 로그들을 수집해서 중앙화 
#### 워커노드 컴포넌트
- kublet 
- kube-proxy
- 컨테이너 런타임 