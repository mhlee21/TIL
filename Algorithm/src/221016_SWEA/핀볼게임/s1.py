import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    change_dir = [[],
                  [1,3,0,2],
                  [3,0,1,2],
                  [2,0,3,1],
                  [1,2,3,0],
                  [1,0,3,2]]

    N = int(input())

    arr = [[5]*(N+2)]
    wormhole_check = [0] * 11
    wormhole_info = dict()
    for i in range(1,N+1):
        arr.append([5] + list(map(int, input().split())) + [5])
        for j in range(1,N+1):
            if 6 <= arr[i][j] <= 10:
                num = arr[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else:  # 같은 번호 웜홀끼리 위치 정보 저장
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]
    arr.append([5]*(N+2))

    def bfs(si,sj,dir):
        score = 0
        ni, nj = si, sj
        while True:
            ni += di[dir]
            nj += dj[dir]
            if (ni, nj) == (si, sj) or arr[ni][nj] == -1:
                return score
            elif 1 <= arr[ni][nj] <= 5:
                dir = change_dir[arr[ni][nj]][dir]
                score += 1
            elif 6 <= arr[ni][nj] <= 10:
                ni,nj = wormhole_info[(ni,nj)]


    # 게임판 위에서 출발 위치와 진행 방향을 임의로 선정가능 할 때,
    # 게임에서 얻을 수 있는 점수의 최댓값을 구하여라
    answer = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] == 0:
                for k in range(4):
                    answer = max(answer, bfs(i,j,k))

    print(f'#{test_case} {answer}')