## static pod 만들기
- control-plane master
  - worker node 1
  - worker node 2
- api는 etcd 정보활용해서 스케쥴러에게 
- 스케쥴러는 가장 적절한 워커노드를 고름 -> api에게 응답
- kublet demon에 의해 실행되는 파드를 static pod라고 부름 
- static pod in etc/kubernetes/manifests
  - 스케쥴러에 의해 x, kublet에 의해 



