import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # 집의 개수
    home = [list(map(int, input().split())) for _ in range(N)]
    town = [[0]*31 for _ in range(31)]
    answer = float("inf")


    # 집에서 충전소까지의 거리를 구하는 함수
    def get_dist(hi,hj,ci,cj):
        return abs(hi-ci) + abs(hj-cj)

    def check(num, charge):
        # num : 충전소 개수
        # charge : 충전소 좌표
        # return : 충전소까지의 거리 (도달하지 못하는 경우 float("inf") 리턴)
        total = 0
        for hi, hj, dist in home:
            # 좌표에 표시하기 위해 15를 더해준다.
            hi += 15
            hj += 15
            dd = float("inf")
            for ci,cj in charge:
                tmp_dd = get_dist(hi,hj,ci,cj)
                if dist < tmp_dd:
                    if num == 1:
                        return float("inf")
                    else:
                        continue
                dd = min(dd, tmp_dd)
            if dd == float("inf"):
                return dd
            total += dd
        return total

    # 집 표시
    for hi, hj, dist in home:
        # 좌표에 표시하기 위해 15를 더해준다.
        hi += 15
        hj += 15
        town[hi][hj] = -1

    # 충전소가 하나인 경우 첫번째 집을 기준으로 검사
    si, sj, sdist = home[0]
    si += 15
    sj += 15
    for dd in range(1, sdist+1):
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni = si + (di*dd)
            nj = sj + (dj*dd)
            # 범위 벗어나거나 집인 경우
            if 0 > ni or ni >30 or 0 > nj or nj >30 or town[ni][nj] == -1:
                continue
            answer = min(answer, check(1, [[ni, nj]]))

    clist = []
    def get_clist(dep,si,sj):
        global answer
        if dep == 2:
            # 충전소까지의 거리 검사
            answer = min(answer, check(2, clist))
            return
        if dep == 1:
            for i in range(si,31):
                for j in range(31):
                    if si == i and sj <= j:
                        continue
                    if not town[i][j]:
                        clist.append([i, j])
                        get_clist(dep+1, i, j)
                        clist.pop(-1)

    # 충전소가 두개인 경우
    if answer == float("inf"):
        for i in range(31):
            for j in range(31):
                if town[i][j] == 0:
                    clist.append([i,j])
                    get_clist(1, i, j)
                    clist.pop(-1)

    # 전기 자동차를 보급 할 수 없는 집이 생길 경우
    if answer == float("inf"):
        answer = -1

    print(f"#{test_case} {answer}")