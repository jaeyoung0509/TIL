input = [
    {"id" :1 , "age":30},
    {"id" :2 , "age":20},
    {"id" :3 , "age":50},
    {"id" :4 , "age":50},
    {"id" :5 , "age":10},
    {"id" :6 , "age":30}
]

def _filter(input: list , predi:callable):
    new_list = []
    for i in  input:
        if(predi(i)):
            new_list.append(i)
    return new_list


def _map(input: list , mapper:callable):
    new_list = []
    for i in input:
        new_list.append(mapper(i))
    return new_list

over_30 = _filter(input, lambda x : x["age"] >=30)
ids = _map(over_30 , lambda x: x["id"])

print(_map(
    _filter(input, lambda x : x["age"] >=30) ,
    lambda x: x["id"])
)