input = [
    {"id" :1 , "age":30},
    {"id" :2 , "age":20},
    {"id" :3 , "age":50},
    {"id" :4 , "age":50},
    {"id" :5 , "age":10},
    {"id" :6 , "age":30}
]

def filter_(input: list , predi:callable):
    new_list = []
    for i in  input:
        if(predi(i)):
            new_list.append(i)
    return new_list

print(filter_(input, lambda x : x["age"] >=30))
print(filter_(input, lambda x : x["age"] <30))
