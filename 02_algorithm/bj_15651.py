# N과 M(3)
# https://www.acmicpc.net/problem/15651

def solve(dep):
    if dep == m:
        print(' '.join(map(str,out)))
        return
    for i in range(1,n+1):
        out.append(i)
        solve(dep + 1)
        out.pop()

n, m = map(int, input().split())
out = []
solve(0)