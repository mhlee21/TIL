# 15분

def solution(grade):
    answer = 0
    for idx in range(1,len(grade)):
        if grade[idx-1] > grade[idx]:                   # 앞의 점수가 현재 점수보다 큰 경우
            for i in range(idx):                        # 이전 점수들을 모두 현재 점수와 같게 만들어주고 그 차이를 저장한다.
                if grade[i] > grade[idx]:
                    answer += (grade[i] - grade[idx])
                    grade[i] = grade[idx]
    return answer

print(solution([2,1,3]))
print(solution([1,2,3]))
print(solution([3,2,3,6,4,5]))
print(solution([5,4,3,2,1]))