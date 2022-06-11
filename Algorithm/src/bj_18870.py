# 백준 18870 [좌표 압축]
# https://www.acmicpc.net/problem/18870
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
N = input()
li = list(map(int,input().split())) # 공백 한 칸으로 구분된 X1, X2, ..., XN

tmp = sorted(list(set(li))) # 중복값 제거하여 정렬

# 시간 단축을 위해 딕셔너리 인덱싱 이용
dic = {tmp[i]:i for i in range(len(tmp))}
for num in li:
    print(dic[num], end=' ')

# [시간 초과한 방법]
# # input li의 요소와 tmp의 요소가 같은경우 li의 요소에 tmp의 인덱스 값을 넣음
# for num in [tmp.index(n) for i, n in enumerate(li)]:
#     print(num, end=' ')