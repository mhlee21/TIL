import time
from datetime import timedelta
start = time.process_time()

# memoization
dp = dict()

def fib(n):
    if n <= 1:
        return n
    if n in dp.keys():
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]

print(fib(5))

end = time.process_time()
print("Time elapsed: ", timedelta(seconds=end-start))