import time
from datetime import timedelta
start = time.process_time()

# tabulation
dp = dict()

def fib(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

print(fib(5))

end = time.process_time()
print("Time elapsed: ", timedelta(seconds=end-start))