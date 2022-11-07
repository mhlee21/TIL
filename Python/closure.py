def times_multiply(n):
    def multiply(x):
        return n * x
    return multiply

times_3 = times_multiply(3)
times_4 = times_multiply(4)

print(times_3, times_4)

print(times_3(5))
print(times_4(5))

del(times_multiply)

print(times_3(5)) # 원 함수에 어떤 변화가 발생되어도 자신의 스코프는 지킨다

print(times_4.__closure__[0].cell_contents)

#======================

