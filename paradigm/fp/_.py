from itertools import gro

def _filter(input: list , predi:callable):
    new_list = []
    if (val:=_each(input, lambda x: predi(x))):
        new_list.append(val)
    return new_list



def _map(input: list , mapper:callable):
    new_list = []
    _each(input , lambda x: new_list.append(mapper(x)))
    return new_list


def _each(input , iter):
    for i in range(len(input)):
        iter(input[i])
    return input

