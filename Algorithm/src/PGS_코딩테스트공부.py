'''
PGS
코딩테스트공부
레벨3
-
https://school.programmers.co.kr/learn/courses/30/lessons/118668?language=python3
'''
'''
시간복잡도
https://blog.chulgil.me/algorithm/
다익스트라 알고리즘
https://gyoogle.dev/blog/algorithm/Dijkstra.html

다익스트라 알고리즘은 특정한 정점에서 다른 모든 정점으로 가는 최단 경로를 기록한다.

다익스트라를 구현하기 위해 두가지를 저장해야한다.
1. 해당 정점까지의 최단거리를 저장 (시작 정점으로부터 정점들의 최단거리를 저장하는 배열)
2. 정점을 방문했는지 저장 (방문 체크 배열)

다익스트라 알고리즘의 순서는 아래와 같다.
1. 최단 거리 값은 무한대 값으로 초기화 한다.
2. 시작 정점의 최단거리는 0이다. 그리고 시작 정점을 방문처리 한다.
3. 시작 정점과 연결된 정점들의 최단거리 값을 갱신한다.
4. 방문하지 않은 정점 중 최단거리가 최소인 정점을 찾는다.
5. 찾은 정점을 방문체크로 변경 후, 해당 정점과 연결된 방문하지 않은 정점의 최단거리 값을 갱신한다.

플로이드 워샬 알고리즘
- 그래프에서 모든 정점 사이의 최단거리를 구하는 알고리즘
- 2차원 배열을 이용하여 동적계획법으로 최적의 값을 계산한다.
'''

def solution(alp, cop, problems):
    '''
    알고력과 코딩력을 높이는 방법
    1. 시간을 들여 알고리즘/코딩공부를 한다.
    2. 현재 풀 수 있는 문제 중 하나를 풀어 알고력/코딩력을 높인다. 문제는 여러번 풀 수 있다.
    '''
    max_alp = 0
    max_cop = 0
    # 문제 중 가장 큰 알고력, 코딩력 구하기
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    # 현재 알고력과 코딩력이 max 값보다 큰 경우 고려
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')
    dp = [[INF]*(max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0 # 현재 알고력, 코딩력을 0으로 초기화

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 알고력을 1 증가시키거나, 코딩력을 1 증가시킬 경우 걸리는 시간 계산
            if i + 1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 현재 알고력과 코딩력으로 풀수 있는 문제인 경우
                if i>=alp_req and j>=cop_req:
                    next_alp = min(max_alp, i+alp_rwd) # 최대 알고력과 증가시킬 수 있는 알고력 비교
                    next_cop = min(max_cop, j+cop_rwd) # 최대 코딩력과 증가시킬 수 있는 코딩력 비교
                    # 증가한 알고력과 코딩력 dp 에 현재 알고력 코딩력 + cost 값을 초기화
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    # 최대 알고력과 코딩력일 때 문제를 다 푸는데 걸린 최소 시간
    return dp[-1][-1]

print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))
# print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))