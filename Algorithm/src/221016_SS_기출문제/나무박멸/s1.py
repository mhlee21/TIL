'''
나무박멸
https://www.codetree.ai/frequent-problems/tree-kill-all/description
'''
import sys
from pprint import pprint

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m, k, c = map(int, input().split())
    forest = [list(map(int, input().split())) for _ in range(n)]
    deadly_ground = [[0]*n for _ in range(n)]
    answer = 0

    # 1단계 : 나무 성장
    def growth(arr):
        for i in range(n):
            for j in range(n):
                if arr[i][j] > 0:
                    cnt = 0 # 나무가 있는 칸 갯수 세기
                    for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                        ni = i + di
                        nj = j + dj
                        if 0 > ni or ni >= n or 0 > nj or nj >= n or arr[ni][nj] <= 0:
                            continue
                        cnt += 1
                    arr[i][j] += cnt
        return arr

    # 2단계 : 나무 번식
    def breeding(arr):
        res = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if arr[i][j] == -1:
                    res[i][j] = arr[i][j]

                # 나무가 있는 칸일 때
                if arr[i][j] > 0:
                    cnt = 0 # 나무가 없는 칸 갯수 세기
                    q = [] # 나무가 없는 칸 위치 저장
                    for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                        ni = i + di
                        nj = j + dj
                        if 0 > ni or ni >= n or 0 > nj or nj >= n \
                                or arr[ni][nj] != 0 \
                                or deadly_ground[ni][nj] > 0:
                            continue
                        if arr[ni][nj] == 0:
                            cnt += 1
                        q.append([ni,nj])

                    # 새로운 지도에 나무 옮기기
                    res[i][j] = arr[i][j]
                    if cnt > 0:
                        tree = arr[i][j]//cnt # 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식, 나눌때 생기는 나머지는 버림
                        while q:
                            ni, nj = q.pop()
                            res[ni][nj] += tree
        return res

    # 3단계 : 나무 박멸
    def kill(arr):
        global answer
        max_ground = 0
        row, col = 0, 0
        for i in range(n):
            for j in range(n):
                # 제초제 유효기간 카운팅
                if deadly_ground[i][j] > 0:
                    deadly_ground[i][j] -= 1

                # 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸 찾기
                if arr[i][j] > 0:
                    cnt = arr[i][j] # 박멸되는 나무 수 카운팅 위한 변수
                    for di, dj in [[-1,-1],[-1,1],[1,-1],[1,1]]:
                        ni, nj = i, j
                        for _ in range(k): ### 제초제의 확산 범위
                            ni += di
                            nj += dj
                            if 0 > ni or ni >= n or 0 > nj or nj >= n or arr[ni][nj] <= 0:
                                break
                            cnt += arr[ni][nj]
                    if cnt > max_ground:
                        max_ground = cnt
                        row, col = i, j

        answer += max_ground

        # 제초제 뿌리기
        if arr[row][col] > 0:
            arr[row][col] = 0
            deadly_ground[row][col] = c
            for di, dj in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
                ni, nj = row, col
                for _ in range(k): ### 제초제의 확산 범위
                    stop = False
                    ni += di
                    nj += dj
                    if 0 > ni or ni >= n or 0 > nj or nj >= n:
                        break
                    if arr[ni][nj] <= 0:
                        # 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우,
                        # 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
                        stop = True
                    if arr[ni][nj] > 0:
                        arr[ni][nj] = 0
                    deadly_ground[ni][nj] = c
                    if stop:
                        break
        return arr

    for y in range(m):
        forest = growth(forest) # 1단계 : 나무 성장
        forest = breeding(forest) # 2단계 : 나무 번식
        forest = kill(forest) # 3단계 : 나무 박멸

    print(f'#{test_case} {answer}')