def add(a,b):
    return a+ b

def execute(func , *args):
    return func(*args)

f = add

print(execute(f, 3, 5))