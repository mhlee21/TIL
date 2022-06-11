---
title: 'algo>BOJ_2615(오목,실버2)'
date: 2022-02-27 21:44:52
categories: 
- algo_python
tags:
- algorithm
- BOJ
- brute force
---

[https://www.acmicpc.net/problem/2615](https://www.acmicpc.net/problem/2615)

문제를 풀기 위해서 처음에 얼마나 규칙을 잘 정하고, 예외처리를 잘 하느냐가 중요한 것 같다.

1. 승리한 경우 가장 왼쪽에 있는 바둑알을 검사하기 위해 오른쪽, 아래 방향으로만 검사할 것
2. 오목이 아닌 육목일 경우 (앞에 하나 더 있는지, 뒤에 하나 더 있는지) 검사 필요
3. 승부가 나지 않는 경우 print(0)을 잊지말자
4. 오목의 갯수 세는 변수인 cnt 의 위치 중요 (방향이 달라지면 새로 카운트하기 위해 꼭 1로 초기화 해줘야한다!)

```python
import sys
input = sys.stdin.readline

def omok():
    di = [-1, 0, 1, 1] # 우상, 우, 우하, 하
    dj = [1, 1, 1, 0]
    for i in range(0, N):  # 15번째 줄까지만 검사하면 됨
        for j in range(0, N):
            check = arr[i][j]
            if check:
                for dr, dc in zip(di, dj):
                    cnt = 1 # 방향 달라질 때 마다 새로 카운트해야함!!
                    row = i + dr
                    col = j + dc
                    # 인덱스 범위 내에 있고, check 와 같은 색의 돌이 있으면
                    while 0 <= row < N and 0 <= col < N and arr[row][col] == check:
                        cnt += 1
                        if cnt == 5:
                            if 0 <=i-dr< N and 0<=j-dc<N and arr[i-dr][j-dc] == check: 
                            # 앞쪽에 하나 더 있는지 검사
                                break
                            if 0 <=row+dr< N and 0<=col+dc<N and arr[row+dr][col+dc] == check: 
                            # 뒤쪽에 하나 더 있는지 검사
                                break
                            # 모두 아니면 결과 출력하고 return 으로 함수 종료
                            print(check)
                            print(i+1, j+1)
                            return
                        row += dr
                        col += dc

    # 승부가 결정되지 않았을 경우에는 0을 출력
    print(0)

N = 19
arr = [list(map(int, input().split())) for _ in range(N)]
omok()
```

