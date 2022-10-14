import sys
from pprint import pprint

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    # 점수 계산하기
    def solve():
        g_num = 0
        group = [[0]*N for _ in range(N)]
        group_list = [0]*(N*N+1) # 1 ~ N*N 까지 그룹 번호 매기기

        def dfs(si,sj):
            nonlocal g_num
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni = si + di
                nj = sj + dj
                if 0 > ni or ni >= N or 0 > nj or nj >= N \
                    or visited[ni][nj] or arr[si][sj] != arr[ni][nj]:
                    continue
                visited[ni][nj] = True
                group[ni][nj] = g_num
                group_list[g_num] += 1
                dfs(ni,nj)

        # visited 초기화
        for i in range(N):
            for j in range(N):
                visited[i][j] = False

        # 그룹 구하기
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] == True
                    g_num += 1
                    group[i][j] = g_num     # 그룹 번호 매기기
                    group_list[g_num] = 1   # 그룹별 갯수 구하기
                    dfs(i,j)

        # 점수 계산
        score = 0
        for i in range(N):
            for j in range(N):
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni = i + di
                    nj = j + dj
                    if 0 > ni or ni >= N or 0 > nj or nj >= N \
                        or arr[i][j] == arr[ni][nj]:
                        continue
                    gnum1, gnum2 = group[i][j], group[ni][nj]
                    gcnt1, gcnt2 = group_list[gnum1], group_list[gnum2]
                    score += (gcnt1 + gcnt2) * arr[i][j] * arr[ni][nj]
        pprint(arr)
        pprint(group)
        print(group_list)
        print(score//2)
        return score // 2 # 중복계산 제외


    # 회전하기
    def rotate(arr_in):
        arr_out = [[0]*N for _ in range(N)]
        num = N//2

        # 십자모양 반시계방향으로 회전
        for i in range(N):
            arr_out[num][i] = arr_in[i][num]
            arr_out[i][num] = arr_in[num][N-1-i]

        # 십자모양을 제외한 4개의 정사각형 개별적으로 회전
        def rotate_90(si,sj,slen):
            for i in range(si, si+slen):
                for j in range(sj, sj+slen):
                    ni, nj = i-si, j-sj                     # 좌표 기준을 0,0으로 변환
                    ri, rj = nj, slen-1-i                   # 90도 회전
                    arr_out[ri+si][rj+sj] = arr_in[i][j]    # 원래자리에 값 넣기

        square_len = N//2
        rotate_90(0,0,square_len)
        rotate_90(0,square_len+1,square_len)
        rotate_90(square_len+1,0,square_len)
        rotate_90(square_len+1,square_len+1,square_len)

        return arr_out


    answer = 0
    for _ in range(4):
        # 점수 계산
        answer += solve()
        # 회전
        arr = rotate(arr)

    print(f'#{test_case} {answer}')