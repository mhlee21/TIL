# 2022.02.02
# 소수 구하기
# https://www.acmicpc.net/problem/1929

# # 방법 1. 해당 수보다 작은 모든 수로 나누기
#
# 메모리 : 30864KB, 시간 : 6408ms
#
# M, N = map(int, input().split())
# for num in range(M, N+1):
#     is_prime = True
#     # 1은 소수가 아님
#     if num == 1:
#         is_prime = False
#         continue
#     # 제곱근까지만 검사하면 됨
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# 방법 2. 에라토스테네스의 체
# 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법
# 참고 : https://wikidocs.net/21638
#
# 메모리 : 38532KB, 시간 : 352ms
#
M, N = map(int, input().split())
is_prime = [True] * (N + 1)

for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(2*i, N+1, i):
            is_prime[j] = False

for i in range(M, N+1):
    if i>1 and is_prime[i]:
        print(i)