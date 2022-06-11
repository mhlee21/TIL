# 백준 1051 [숫자 정사각형]
# https://www.acmicpc.net/problem/1051
# N x M 크기의 직사각형
n, m = map(int, input().split())
arr = [input().strip() for i in range(n)]

ret = 1
for i in range(n):
    for j in range(m):
        for k in range(j+1,m):
            # 같은 줄에서 같은 숫자를 가진 칸이 있는 경우
            if arr[i][j] == arr[i][k]:
                len = k - j
                # 직사각형이 되는지 검사
                if (i+len) < n and arr[i][j] == arr[i+len][j] == arr[i+len][k]:
                    # 최대값인 경우 저장
                    ret = max(ret, (len+1)**2)
print(ret)