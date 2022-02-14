# N과 M(2)
# https://www.acmicpc.net/problem/15650

from pydoc import visiblename


N, M = map(int, input().split())

def solve(start):
    if visited.count(True) == M:
        print(' '.join(map(str,out)))
        return
    
    for i in range(start,N+1):
        if not visited[i]:
            visited[i] = True
            out.append(i)
            solve(i+1)
            visited[i] = False
            out.pop()

visited = [False] + [False for _ in range(N)]
out = []
solve(1)