"""
PGS
순위 검색
level2
2시간
https://programmers.co.kr/learn/courses/30/lessons/72412
"""

### 정확성 통과, 효율성 실패 ###
# def solution(info, query):
#     applicant = []
#     for i in info:
#         applicant.append(i.split())
#     answer = []
#     for q in query:
#         qq = q.split()
#         res = []
#         for a in applicant:
#             if int(a[-1]) >= int(qq[-1]):       # 점수 비교
#                 for idx in range(len(a)-1):     # 점수 외 다른 조건 비교
#                     if qq[idx*2] == '-':
#                         continue
#                     if a[idx] != qq[idx*2]:
#                         break
#                 else:                           # 모두 통과한 경우 res에 추가
#                     res.append(a)
#         answer.append(len(res))                 # res에 추가된 지원자의 수 answer에 저장
#     return answer

### 정확성 통과, 효율성 통과 ###
# combinations: 리스트의 모든 조합 구하기
# defaultdict: 유사 딕셔너리, defaultdict 사용하지 않으면 키가 있는지 여부와 초기화 하는 코드가 필요하다.
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in info:
        temp = i.split()
        # key 값과 score 로 분리
        key = temp[:-1]
        score = int(temp[-1])

        # info 의 모든 경우의 수를 info_dict 의 key 값으로 저장
        for leng in range(5):
            combi = list(combinations(key, leng))
            for c in combi:
                temp_key = ''.join(c)
                info_dict[temp_key].append(score)

    # 각 경우의 수에 해당하는 점수들을 오름차순 정리
    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split()
        # key 값과 score 로 분리
        q_key = q[:-1]
        q_score = int(q[-1])

        for _ in range(3):
            q_key.remove("and")
        while "-" in q_key:
            q_key.remove("-")
        q_key = ''.join(q_key)

        if q_key in info_dict:
            score_list = info_dict[q_key]

            if len(score_list) > 0:
                # 이분탐색 - Lower bound
                left, right = 0, len(score_list)
                while left < right:
                    mid = (left + right) // 2
                    if score_list[mid] >= q_score:
                        right = mid
                    else:
                        left = mid + 1
                answer.append(len(score_list)-left)
        else:
            answer.append(0)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))