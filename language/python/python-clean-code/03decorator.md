### 데코레이터
- 함수에 변형을 할 때마다 modifier 함수를 사용하여 함수를 호출한 다음 
함수를 처음 정의한 것 과 같은 이름으로 재할당
```python
def original():
    ...
original =  modifier(original)

@modifier
def original():
    ...
```
- 데코레이터 이후에 나오는 것을 데코레이터의 첫번째 파라미터로 하고
데코레이터의 결과 값을 반환하게 하는 문법적 설탕 (syntax sugar)
- modifer : decorator function
- original: wrapped or decorated object
- 데코레이터 디자인 패턴과 혼동하면 안됨
```python
class ControlledException(Exception):
    ""도메인에서 발생하는 일반적인 예외""
    ...

def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        RETIRES_LIMIT = 3
        for _ in range(RETIRES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ControlledException as e:
                last_raised = e
            raise last_raised
        return wrapped
```