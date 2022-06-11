# 2021.01.27
# 백준 2529 [부등호]
# https://www.acmicpc.net/problem/2529

k = int(input())
arr = input().split()

visited = [0]*10
mx, mn = '', ''

def check(i,j,k):
    if k == '>':
        return i>j
    else:
        return i<j

def solve(idx, n_str):
    global mx, mn
    if idx == (k + 1):
        if len(mn) == 0:
            mn = n_str
        else:
            mx = n_str
        return
    else:
        for i in range(10):
            if not visited[i]:
                if (idx == 0) or check(int(n_str[-1]), i, arr[idx-1]):
                    visited[i] = True
                    solve(idx+1, n_str+str(i))
                    visited[i] = False

solve(0, '')
print(mx)
print(mn)