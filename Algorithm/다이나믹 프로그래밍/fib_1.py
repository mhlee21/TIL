import time
from datetime import timedelta
start = time.process_time()

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))

end = time.process_time()
print("Time elapsed: ", timedelta(seconds=end-start))