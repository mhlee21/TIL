# 1시간 30분
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())    # 낚시터의 개수
    v = [0]*N           # 방문 체크 배열
    fisher = [list(map(int, input().split())) for _ in range(3)]
    gate = [0]*3
    result = float('inf')

    def check_spot(g_num, f_num, r):
        ret = 0
        ret2 = []
        dist = 0
        flag = -1

        while f_num:
            x = g_num + (dist * flag)
            if 0 <= x < N and v[x] == 0:
                v[x] += r
                ret += dist + 1
                f_num -= 1

            # 오른쪽 확인
            flag *= -1

            # 왼쪽 -> 오른쪽 -> 다시 왼쪽인 경우 다음칸 검사
            if flag < 0 and f_num != 0:
                dist += 1

            # 마지막 사람이 왼쪽 들어간 경우, 오른쪽에 들어갈 수 있는지 체크
            if flag > 0 and f_num == 0:
                x2 = g_num + (dist * flag)
                if 0 <= x2 < N and v[x2] == 0:
                    ret2 = [x, x2]

        return ret, ret2


    def my_dfs(n, total):
        global result
        if n == 3:
            if total < result:
                result = total
            return
        for i in range(3):
            if gate[i]:
                continue
            gate[i] = 1
            ret, ret2 = check_spot(fisher[i][0]-1, fisher[i][1], i+1)
            my_dfs(n+1, total+ret)

            if ret2:
                v[ret2[0]] = 0
                v[ret2[1]] = i+1
                my_dfs(n+1, total+ret)
                # v[ret2[1]] = 0
                # v[ret2[0]] = i+1

            for j in range(N):
                if v[j] == i+1:
                    v[j] = 0
            gate[i] = 0

    my_dfs(0,0)
    print(f'#{test_case} {result}')