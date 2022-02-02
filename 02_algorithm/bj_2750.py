# 2022.02.02
# 수 정렬하기
# https://www.acmicpc.net/problem/2750

N = int(input())
arr = list(map(int, [input() for i in range(N)]))

#Bubble Sort
for i in range(N):
    for j in range(i,N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for a in arr:
    print(a)