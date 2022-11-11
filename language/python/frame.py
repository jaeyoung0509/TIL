import inspect
frame = None
def func():
    global frame
    x = 10
    y = 20
    print(x+y)
    frame = inspect.currentframe

func()