######################################################
# clouser
######################################################
def times_multiply(n):
    def multiply(x):
        return n * x
    return multiply

times_3 = times_multiply(3)
times_4 = times_multiply(4)

print(times_3, times_4)

print(times_3(5))
print(times_4(5))

del(times_multiply) # times_multiply 를 메모리 상에서 삭제

print(times_3(5)) # 원 함수에 어떤 변화가 발생되어도 자신의 스코프는 지킨다

print(times_4.__closure__[0].cell_contents)

######################################################
'''
decorator
- 함수를 다른 함수의 인자로 전달하려 기존 객체에 새로운 기능을 추가할 수 있도록 하는 python 의 디자인 패턴
'''
######################################################

def trace(func): # 함수 안에서 함수를 만들고 반환하는 클로저
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper

def trace2(func): # 함수 안에서 함수를 만들고 반환하는 클로저
    def wrapper():
        print(func.__name__, '함수 시작2')
        func()
        print(func.__name__, '함수 끝2')
    return wrapper

@trace
@trace2
def hello():
    print('안녕하세요')

# trace_hello = trace(hello)
# trace_hello()
hello()

def foo(a: dict={}):
    if 'x' not in a.keys():
        