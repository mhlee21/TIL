import time
from datetime import timedelta
start = time.process_time()

# 두 변수만 이용해 공간 절약
def fib(n):
    x, y = 0, 1
    for i in range(0,n):
        x,y = y, x+y
    return x

print(fib(5))

end = time.process_time()
print("Time elapsed: ", timedelta(seconds=end-start))