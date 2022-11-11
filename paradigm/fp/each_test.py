from _ import _each, _filter ,_map
input = [
    {"id" :1 , "age":30},
    {"id" :2 , "age":20},
    {"id" :3 , "age":50},
    {"id" :4 , "age":50},
    {"id" :5 , "age":10},
    {"id" :6 , "age":30}
]
print(_map(
    _filter(input, lambda x : x["age"] >=30) ,
    lambda x: x["id"])
)

iter()
