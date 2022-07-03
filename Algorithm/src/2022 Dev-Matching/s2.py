# 35분

def solution(n, horizontal):
    answer = [[0]*n for _ in range(n)]
    answer[0][0] = 1
    for i in range(1, n+1):
        num = i*i - (i-1)
        answer[i-1][i-1] = num          # 오른쪽 아래 모서리 값 먼저 채우기
        if (i-1) % 2:                   # 홀수 인덱스 채우기 (1,1), (3,3), ...
            cnt = 1
            for idx in range(i - 1, 0, -1):
                if horizontal:
                    answer[idx - 1][i - 1] = num - cnt
                    answer[i - 1][idx - 1] = num + cnt
                else:
                    answer[i - 1][idx - 1] = num - cnt
                    answer[idx - 1][i - 1] = num + cnt
                cnt += 1
        else:                           # 짝수 인덱스 채우기 (2,2), (4,4), ...
            cnt = 1
            for idx in range(i - 1, 0, -1):
                if horizontal:
                    answer[idx - 1][i - 1] = num + cnt
                    answer[i - 1][idx - 1] = num - cnt
                else:
                    answer[i - 1][idx - 1] = num + cnt
                    answer[idx - 1][i - 1] = num - cnt
                cnt += 1
    return answer

print(solution(4, True))
print(solution(5, False))