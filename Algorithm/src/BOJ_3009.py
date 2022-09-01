'''
BOJ
네 번째 점
브론즈3
10분
https://www.acmicpc.net/problem/3009
'''
left = []
right = []
for _ in range(3):
    n1, n2 = map(int, input().split())
    if n1 in left:
        left.remove(n1)
    else:
        left.append(n1)
    if n2 in right:
        right.remove(n2)
    else:
        right.append(n2)

print(*left, *right)