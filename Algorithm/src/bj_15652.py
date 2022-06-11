# N과 M(4)
# https://www.acmicpc.net/problem/15652

def solve(start,dep):
    if dep == m:
        print(' '.join(map(str,out)))
        return
    for i in range(start,n+1):
        out.append(i)
        solve(i,dep+1)
        out.pop()

n, m = map(int,input().split())
out = []
solve(1, 0)