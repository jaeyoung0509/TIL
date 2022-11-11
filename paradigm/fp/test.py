# map return an iterator that yields the results
# map(<f> , <iterable>)
# map returns a iterator called a map object 
li = [i for i in range(1, 9, 1)]
func = lambda x: x**2
t = list(map(func, li))
print(li)
print(t)

# calling map()_ with multiple iterables
# map(<f> , <iterable> , <iterable> , <iterable> , <iterable> , <iterable>)
t = list(map((lambda x,y,z : x+y+z), [1,2,3],[10,20,30], [100 , 200, 300]))
print(t) 


# filter 
# filter(<f> , <iterable>)
t = list(filter(lambda x: x> 100 , [100 , 200, 300]))
print(t)

# reducing an iterable to a single value with reduce()
# reduce(<f> , <iterable>)
from itertools import reduce 
# reduce(<f> , <iterable> , <init_value>)

