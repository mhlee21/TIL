# 백준 11792 [하노이 탑 이동 순서]
# https://www.acmicpc.net/problem/11729
# 제일 밑에 있는 층이 목표인 3번 기둥으로 간다.
# 그 위의 층은 다른 기둥인 2번으로 간다.
# 다시 그 위의 층은 앞의 기둥과 다른 3번 기둥으로 간다.
# ex) 3층인 탑 -> 3,2,3 -> 제일 처음 3번 기둥으로 가면 된다.

# 더 간단 하게, 원판의 갯수가 n개 라고 할 경우,
# 출발(a), 임시(b), 목적지(c) 막대가 있다.
# 1. a 에 있는 n-1개의 원판을 b로 옮긴다.
# 2. a 에 있는 제일 밑의 원판을 c 로 옮긴다.
# 3. b 에 있는 n-1개의 원판을 c로 옮긴다.

n = int(input())
ret = []

def solve(n, a, b, c):
    if n == 1:
        ret.append([a, c])
    else:
        solve(n-1, a, c, b)
        ret.append([a, c])
        solve(n-1, b, a, c)

solve(n, 1, 2, 3)
print(len(ret))
for x, y in ret:
    print(x, y)