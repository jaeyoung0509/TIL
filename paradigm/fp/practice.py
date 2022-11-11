from functools import reduce
def compose(func1 : callable, func2 : callable) -> callable:
    return lambda x : func2(func1(x))

users : list[dict] = [
    {"id" : 101 , "name" : "ID"},
    {"id": 102, "name": "IDX"},
    {"id": 103, "name": "IAD"},
    {"id": 104, "name": "IWD"},
    {"id": 105, "name": "FID"},
    {"id": 106, "name": "WID"},
]

posts : list[dict] = [
    {"id" : 201 , "body" : "내용1" ,"user_id" : 101},
    {"id": 202, "body": "내용2", "user_id": 102},
    {"id": 203, "body": "내용3", "user_id": 103},
    {"id": 204, "body": "내용4", "user_id": 102},
    {"id": 205, "body": "내용5", "user_id": 101},
]

comments : list[dict] = [
    {"id" : 301 , "body" : "댓글1" , "user_id" :105 , "post_id" :201},
    {"id": 302, "body": "댓글2", "user_id": 104, "post_id": 201},
    {"id": 303, "body": "댓글3", "user_id": 104, "post_id": 201},
    {"id": 304, "body": "댓글4", "user_id": 105, "post_id": 202},
    {"id": 305, "body": "댓글5", "user_id": 106, "post_id": 203},
    {"id": 306, "body": "댓글6", "user_id": 106, "post_id": 203},
    {"id": 307, "body": "댓글7", "user_id": 102, "post_id": 204},
    {"id": 308, "body": "댓글8", "user_id": 103, "post_id": 205},
    {"id": 309, "body": "댓글9", "user_id": 103, "post_id": 201},
]
map(
    filter(input, lambda x : x["age"] >=30) ,
    lambda x: x["id"])
)
reduce(filter(lambda x :x.get("user_id") ==101 ,posts) ,)
# 1. 특정인의 posts안의 모든 Comments 거르기
a = list(map(filter(lambda x: x.get("user_id") == 101 , posts) , lambda x: x.get("id")))
t =filter(lambda x: x.get("post_id") in a , list(comments))
print(list(a) ,list(t))
# 2. 특정안의 posts안의 comments를 단 친구의 이름들 뽑기
pipes = [lambda x: x.get("user_id") , lambda x : x.get("post_id")]
# c = [filter(reduce(compose ,  pipes) , iter(posts))]
# print(c)
#final = list(map(lambda x: filter(lambda y: y not in filters_exclude, x), initial_list)
# w = list(map(lambda x: filter(lambda y: y.get("post_id") , x)))
#w = map(filter(lambda x: x.get("post_id") , iter(filter(lambda x : x.get("user_id") == 101 ) ,posts)))
# print(w)
#pipes = [filter(lambda x: x.get("user_id") == 101 , posts , filter(lambda  x: x.get("post_id") == ))]
# b = filter(filter(filter(lamb)))
# 3. 특정인의 posts안의 comments를 단 친구들 카운트 정보

# 4. 특정인의 comments를 단 postsr 거르기