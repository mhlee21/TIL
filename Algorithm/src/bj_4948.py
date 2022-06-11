# 2022.02.07
# 베르트랑 공준
# https://www.acmicpc.net/problem/4948

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

def solve(num):
    '''
    자연수 n이 주어졌을 때, 
    n보다 크고, 2n보다 작거나 같은 소수의 개수를 반환하는 함수
    '''

    # 에라토스테네스의 체 (0~2*num 까지 배열 만들기, 0,1,~2*num)
    a = [False, False] + [True]*(2*num-1)

    # 2num 까지 범위에서 합성수 지우기
    # 시간 단축을 위해 2*num 의 절반인 num 까지만 검사
    for i in range(num+1):
        if a[i]:
            for j in range (2*i, 2*num+1, i):
                a[j] = False

    # num 보다 크고 2*num 보다 작거나 같은 소수 찾아서 그 개수를 리턴
    primes = []
    for i in range(num+1, 2*num+1):
        if a[i]:
            primes.append(i)
    return len(primes)

# 입력 값을 nums 배열에 저장, 0인 경우 while 문 종료
nums = []
while True:
    nums.append(int(input()))
    if nums[-1] == 0:
        break

# 입력받은 nums 배열을 검사하여 결과값 출력
for num in nums:
    if num == 0:
        break
    print(solve(num))