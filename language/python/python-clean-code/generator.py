def sequence(name , start , end):
    yield from range(start, end)
    return end

def main():
    step = yield from sequence("first" , 0, 5)
    step2 = yield from sequence("second" , step, 10)
    return step + step2

g = main()
