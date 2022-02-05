# 직사각형 네개의 합집합의 면적 구하기
# https://www.acmicpc.net/problem/2669

r = [list(map(int,input().split())) for i in range(4)]
map =  [[False for i in range(100)] for j in range(100)]

for dot in r:
    for j in range(dot[1], dot[3]):
        for i in range(dot[0], dot[2]):
            map[j][i] = 1

ret = 0
for idx in range(10):
    ret += map[idx].count(1)

print(ret)