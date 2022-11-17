### itertools 활용하기
- islice
  - 반복가능 객체에서 자르고 싶은 만큼 자를 수 있다
- tee
  - 원래의 이터러블을 세 개의 새로운 이터러블로 분할
  - 그리고 구매 이력을 세 번 반복할 필요 없이 분할된 이터러블을 사용해 필요한 연산을 함

### iterable
- `__iter__`
- 이터레이터와 함께 반복 로직을 만든다
- for in 구문 사용 가능

### iterator
- `__next__`
- 한번씩 하나씩 값을 생산하는 로직을 정의
- 더이상 생산할 수 없는 경우는 Stopiteration error occur

### sequence object
- `__iter__`
- `__getitem__` + `__len__`


### 코루틴
- TODO