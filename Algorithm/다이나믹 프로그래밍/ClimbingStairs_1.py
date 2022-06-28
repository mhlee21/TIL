def climb_stairs(n):
    if n == 1 or n == 2:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)

print(climb_stairs(3))
