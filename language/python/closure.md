- non local variable
- python은 import time과 run time이 있음
  https://www.honeybadger.io/blog/memory-management-in-python/
  https://nachwon.github.io/asyncio-futures/
  https://www.youtube.com/watch?v=oLHmoy9bKCY
  https://github.com/lih0905/Fluent_Python
  https://github.com/lih0905/python_multiprocessing/tree/master/Presentation
  https://ziwon.github.io/post/python_magic_methods/https://ziwon.github.io/post/python_magic_methods/

  instance good `__hash__` function https://stackgokr.com/detail/2278
  https://docs.python.org/3/reference/datamodel.html?highlight=__hash__#object.__hash__

### 함수 중첩 (function nesting)
- zen of python에서는 가급적 중첩을 피하라고 이야기
- 하지만 중첩이 필요한 경우도 있음


### first class object
- first class citizens 일급 객체는 
해당 언어내에서 일반적으로 다른 모든 개체에 통용가능한 동작이 지원되는 개체를 의미
1. 함수의 인자로 전달
2. 함수의 반환값으로
3. 수정되고 할당
> cf) c언어에서는 함수의 인자로 함수의 포인터를 전달할 수 있어도 함수의 이름을 전달할 수 는 없음
- 파이썬에서는 함수도 일급 객체
-> 위 특성이 있어야 클로저가 성립 가능


### nonlocal
- global, nonlocal, local 스코프를
- https://shoark7.github.io/programming/python/closure-in-python