# N과 M(1)
# https://www.acmicpc.net/problem/15649

N, M = map(int, input().split())

def solve():
    if visited.count(True) == M:
        print(' '.join(map(str,out)))
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            out.append(i)
            solve()
            visited[i] = False
            out.pop()

visited = [False] + [False for _ in range(N)]
out = []
solve()