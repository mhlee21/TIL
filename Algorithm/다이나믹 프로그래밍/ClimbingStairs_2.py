dp = dict()
def climb_stairs(n):
    if n <= 2:
        # dp[n] = n
        # return dp[n]
        return n
    if n in dp.keys():
        return dp[n]
    dp[n] = climb_stairs(n-1) + climb_stairs(n-2)
    return dp[n]

print(climb_stairs(3))