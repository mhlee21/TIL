# 2022.02.07
# 수 이어가기
# https://www.acmicpc.net/problem/2635

num = int(input())
result = []     # 결과 출력을 위한 배열
len_result = 0  # 결과 출력을 위한 변수

# num : 첫번째 수
# i : 두번째 수
for i in range(num+1):
    tmp = [num, i]
    j = 0

    # 앞의 앞의 수에서 앞의 수를 뺀 결과가 음수가 나올때까지 계산
    while True:
        last = tmp[j] - tmp[j+1]
        j += 1
        if last < 0:
            break
        tmp.append(last)

    # max값과 이때의 배열 저장
    if len_result < len(tmp):
        len_result = len(tmp)
        result = tmp[:]
    ## end of for ##

# 결과 출력
print(len_result)
# print(' '.join(str(r) for r in result))
print(*result) # join 을 쓰지 않아도 unpacking 을 통해 출력 가능함