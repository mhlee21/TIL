import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_core = 0
    min_len = float("inf")


    # 렉시노스에 존재하는 core 찾기
    core = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                core.append([i,j])
    num_core = len(core)


    def my_dfs(dep, core_cnt, core_len):
        global min_len, max_core
        if dep == num_core:
            if core_cnt > max_core:     # 최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이 합 구하기
                max_core = core_cnt
                min_len = core_len
            elif core_cnt == max_core:  # 단, 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값 구하기
                min_len = min(min_len, core_len)
            return

        ci, cj = core[dep]

        # 렉시노스의 가장자리에 위치한 Core는 이미 전원이 연결된 것으로 간주
        if ci == 0 or ci == N-1 or cj == 0 or cj == N-1:
            my_dfs(dep + 1, core_cnt + 1, core_len)

        # core 가 가장자리에 위치하지 않은 경우
        else:
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni = ci
                nj = cj
                dist = 0
                while 0 <= ni + di < N and 0 <= nj + dj < N and arr[ni + di][nj + dj] == 0:
                    dist += 1
                    ni += di
                    nj += dj
                    arr[ni][nj] = 2 # 방문 체크

                # 가장자리 도달하는 경우
                if ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
                    # 재귀 호출
                    my_dfs(dep + 1, core_cnt + 1, core_len + dist)

                # 방문 체크 해제
                while dist and arr[ni][nj] == 2:
                    arr[ni][nj] = 0
                    dist -= 1
                    ni -= di
                    nj -= dj

            # core 연결할 수 없는 경우 다음 코어 검사
            my_dfs(dep + 1, core_cnt, core_len)

    my_dfs(0, 0, 0)

    print(f"#{test_case} {min_len}")