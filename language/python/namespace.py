#네임 스페이스란 프로그래밍 언어ㅔ에서 특정한 객체를 이름에 다라 구분할 수 있는
# 범위를 의미

def outer_space():
    a = 20
    def inner_func():
        a = 30
        print(f"a= {a}")
    inner_func()
    print(f"a= {a}")

a = 10
outer_space()
print(f"a={a}")
