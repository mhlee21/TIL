'''
PGS
성격유형검사하기
레벨1
20분
https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3
'''

def solution(survey, choices):
    check = {"R":0, "T":0, "C":0, "F":0,
             "J":0, "M":0, "A":0, "N":0}

    for i in range(len(survey)):
        score = choices[i] - 4
        if score < 0:
            check[survey[i][0]] += abs(score)
        elif score > 0:
            check[survey[i][1]] += score

    answer = ''
    check_str = ["RT", "CF", "JM", "AN"]
    print(check)
    for cs in check_str:
        if check[cs[0]] >= check[cs[1]]:
            answer += cs[0]
        else:
            answer += cs[1]
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))