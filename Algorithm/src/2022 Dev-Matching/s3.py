# 40분

from collections import deque
def solution(rows, columns, lands):
    arr = [[0]*columns for _ in range(rows)]
    for l in lands:                     # 지도 그리기
        arr[l[0]-1][l[1]-1] = 1
    # 지도의 맨 끝 테두리는 항상 바다
    for r in range(rows):
        arr[r][0] = 3
        arr[r][columns-1] = 3
    for c in range(columns):
        arr[0][c] = 3
        arr[rows-1][c] = 3

    ans_list = []
    for r in range(1,rows-1):
        for c in range(1,columns-1):
            if arr[r][c] == 0:
                ####### 호수 넓이 구하기 (BFS) #######
                q = deque()
                q.append([r,c])
                tmp = []
                arr[r][c] = 2 # 방문체크
                cnt = 1
                while q:
                    i,j = q.popleft()
                    tmp.append([i,j])
                    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= rows or nj < 0 or nj >= columns:
                            continue
                        if 0 < arr[ni][nj] < 3: # 이미 체크한 곳 이거나 육지인 경우
                            continue
                        if arr[ni][nj] == 3:    # 바다인경우
                            for ti, tj in tmp:  # 이전까지의 좌표에 모두 바다 표시
                                arr[ti][tj] = 3
                            cnt = 0
                            break
                        arr[ni][nj] = 2
                        q.append([ni,nj])
                        cnt += 1
                if cnt > 0:
                    ans_list.append(cnt)
                ##################################
    if len(ans_list) == 0:
        return [-1,-1]
    elif len(ans_list) == 1:
        return ans_list*2
    else:
        return [min(ans_list), max(ans_list)]


print(solution(9,7,[[2, 2], [2, 3], [2, 5], [3, 2], [3, 4], [3, 5], [3, 6], [4, 3], [4, 6], [5, 2], [5, 5], [6, 2], [6, 3], [6, 4], [6, 6], [7, 2], [7, 6], [8, 3], [8, 4], [8, 5]]))
print(solution(5, 6, [[2, 2], [2, 3], [2, 4], [3, 2], [3, 5], [4, 3], [4, 4]]))
print(solution(5, 7, [[2, 5], [3, 3], [3, 4], [3, 5], [4, 3]]))