from itertools import islice
# purchases = islice(filter(lambda p : p>1000.0 , purchases) , 10)
from itertools import tee

for i in islice(range(10), 5):
    print (i)


purchases = []
# 1000개 넘개 구매한 이력의 처음 10개만 처리
purchases = islice(filter(lambda p : p>1000.0 , purchases))
# 모든 것이 제너레이터이므로 게으르게 평가 
# 전체에서 필터링한 값으로 연산을 한 것처럼 보이지만 실제로는 하나씩 가져와서 모든것을 메모리에 올릴 필요는 없음

def process_purchases(purchases):
    min_, max_, avg = tee(purchases, 3)