---
title: queue
date: 2022-02-25 09:07:03
categories: 
- algorithm
tags:
- algorithm
- queue
- 선형큐
- 원형큐
- 우선순위큐
- BFS
---

# Queue

* 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조

* 선입선출 (FIFO : First In First Out)
  * 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제된다.

* 큐의 선입선출 구조

  * Front : 마지막으로 삭제된 위치
  * Rear : 마지막으로 저장된 위치

  ![image-20220225090929957](image-20220225090929957.png)

## 큐의 기본 연산

* enQueue (item) : 큐의 뒤쪽 (read 다음) 에 원소를 삽입하는 연산
* deQueue() : 큐의 앞쪽 (front) 에서 원소를 삭제하고 반환하는 연산
* createQueue() : 공백상태의 큐를 생성하는 연산
* isEmpty() : 큐가 공백상태인지를 확인하는 연산
* isFull() : 큐가 포화상태인지를 확인하는 연산
* Qpeek() : 큐의 앞쪽 (front) 에서 원소를 삭제없이 반환하는 연산

## 큐의 연산 과정

![image-20220225091508273](image-20220225091508273.png)

## 선형큐

* 1차원 배열을 이용한 큐
  * 큐의 크기 = 배열의 크기
  * front : 저장된 첫번째 원소의 인덱스
  * rear : 저장된 마지막 원소의 인덱스
* 상태표현
  * 초기상태 : front = rear = -1
  * 공백상태 : front == rear
  * 포화상태 : rear == n-1 (n : 배열의 크기, n-1 : 배열의 마지막 인덱스)

### 선형 큐의 구현

* 초기 공백 큐 생성

  * 크기 n 인 1차원 배열 생성
  * front와 rear 를 -1 로 초기화

* 삽입 : enQueue(item)

  * 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    1. rear 값을 증가시켜 새로운 원소를 삽입할 자리를 마련
    2. 그 인덱스에 해당하는 배열원소 Q[rear] 에 item 을 저장

  ```python
  def enQueue(item):
  	global rear
  	if isFull() : print("Queue_Full")
      else:
          rear <- rear + 1
          Q[rear] <- item
  ```

* 삭제 : deQueue()

  * 가장 앞에 있는 원소를 삭제하기 위해
    1. front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
    2. 새로운 첫번째 원소를 리턴함으로써 삭제와 동일한 기능함

  ```python
  def deQueue():
      if isEmpty():
          Queue_Empty()
      else:
          front <- front + 1
          return Q[front]
  ```

* 공백상태 및 포화상태 검사 : isEmpty(), isFull()

  * 공백상태 : front == rear
  * 포화상태 : rear == n-1

  ```python
  def isEmpty():
      return front == rear
  def isFull():
      return rear == len(Q) - 1
  ```

* 검색 : Qpeek()

  * 가장 앞에 있는 원소를 검색하여 반환하는 연산
  * 현재 front의 한자리 뒤 (front+1) 에 있는 원소, 즉 큐의 첫번째에 있는 원소를 반환

  ```python
  def Qpeek():
      if isEmpty():
          print("Queue_Empty")
      else:
          return Q[front + 1]
  ```

### 선형 큐 이용시 문제점

* 잘못된 포화상태 인식
  * 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, rear = n-1 인 상태 즉, 포화상태로 인식하여 더이상의 삽입을 수행하지 않게 됨
* 해결방법 1
  * 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
  * 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐
* 해결방법 2
  * 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
  * 원형 큐의 논리적인 구조

​	![image-20220225093617600](image-20220225093617600.png)

## 원형 큐

* 초기 공백 상태

  * front = rear = 0

* Index 의 순환

  * front 와 rear의 위치가 배열의 마지막 인덱스인 n-1 을 가리킨 후, 그 다음에 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
  * 이를 위해 나머지 연산자 mod 를 사용함

* front 변수

  * 공백 상태와 포화 상태  구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

* 삽입 위치 및 삭제 위치

  |        | 삽입 위치               | 삭제 위치                 |
  | ------ | ----------------------- | ------------------------- |
  | 선형큐 | rear = rear + 1         | front = front + 1         |
  | 원형큐 | rear = (rear + 1) mod n | front = (front + 1) mod n |

### 원형 큐의 연산 과정

![image-20220225094057288](image-20220225094057288.png)

### 원형 큐의 구현

* 초기 공백 큐 생성

  * 크기 n 인 1차원 배열 생성
  * front와 rear를 0으로 초기화

* 공백상태 및 포화상태 검사 : isEmpty(), isFull()

  * 공백상태 : front == rear
  * 포화상태 : 
    * 삽입할 rear의 다음위치 == 현재 front
    * (rear + 1) mod n == front

  ```python
  def ifEmpty():
      return front == rear
  def isFull():
      return (rear + 1) % len(cQ) == front
  ```

* 삽입 : enQueue(item)

  * 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    1. rear값을 조정하여 새로운 원소를 삽입할 자리를 마련함 : rear <- (rear + 1) mod n
    2. 그 인덱스에 해당하는 배열원소 cQ[rear]에 item을 저장

  ```python
  def enQueue(item):
      global rear
      if isFull():
          print("Queue_Full")
      else:
          rear = (rear + 1) % len(cQ)
          cQ[rear] = item
  ```

* 삭제 : deQueue(), delete()

  * 가장 앞에 있는 원소를 삭제하기 위해
    1. front값을 조정하여 삭제할 자리를 준비함
    2. 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능함

  ```python
  def deQueue():
      global front
      if isEmpty():
          print("Queue_Empty")
      else:
          front = (front + 1) % len(cQ)
          return cQ[front]
  ```

  ```python
  def delete():
      global front
      if isEmpty():
          print("Queue_Empty")
      else:
          front = (front + 1) % len(cQ)
  ```

  

## 우선순위 큐(Priority Queue)

* 우선순위를 가진 항목들을 저장하는 큐
* FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.
* 우선순위 큐의 적용분야
  * 시뮬레이션 시스템
  * 네트워크 트래픽 제어
  * 운영체제의 테스크 스케줄링
* 트리 구조 사용



## 큐의 활용 : 버퍼 (Buffer)

* 버퍼
  * 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  * 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를  채우는 동작을 의미

* 버퍼의 자료구조
  * 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다.
  * 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용된다.

## BFS (Breadth First Search)

* 너비우선탐색
  * 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
  
* 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야하므로, 선입선출 형태의 자료구조인 큐를 활용함

* 다음과 같은 순서로 탐색

  ![image-20220225102143473](image-20220225102143473.png)

  ```python
  def BFS(G, v): # 그래프 G, 탐색 시작점 v
      visited = [0]*(n+1)		# n : 정점의 개수
      queue = []				# 큐 생성
      queue.append(v)		# 시작점 v를 큐에 삽입
      while queue:			# 큐가 비어있지 않은 경우
          t = queue.pop(0)	# 큐의 첫번째 원소 반환
          if not visited[t]		# 방문되지 않은 곳이라면
          	visited[t] = True	# 방문한 것으로 표시
              visit(t)			# 정점 t에서 할일
          for i in G[t]:			# t와 연결된 모든 정점에 대해
              if not visited[i]:	# 방문되지 않은 곳이라면
                  queue.append(i)	# 큐에 넣기
  ```

  ```python
  def BFS(G, v, n): # 그래프 G, 탐색 시작점 v
      visited = [0]*(n+1)		# n : 정점의 개수
      queue = []				# 큐 생성
      queue.append(v)		# 시작점 v를 큐에 삽입
      visited[v] = 1
      while queue:			# 큐가 비어있지 않은 경우
          t = queue.pop(0)	# 큐의 첫번째 원소 반환
          visit(t)
          for i in G[t]:			# t와 연결된 모든 정점에 대해
              if not visited[i]:	# 방문되지 않은 곳이라면
                  queue.append(i)	# 큐에 넣기
                  visited[i] = visited[n] + 1 # n으로 부터 1만큼 이동
  ```

  

* 탐색의 목적에 따라 DFS/BFS 적절히 활용하면 중복 탐색을 줄일 수 있다.
  
  * ex) 최단거리는 DFS

### 미로탐색 (SWEA 5105)

* 출발-도착 최소 이동거리

```
1
5
13101
10101
10101
10101
10021
```

```bash
#1 5
```

```python
# bfs
def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
	return -1, -1 # 못찾으면 -1 리턴

def bfs(i,j,N):
    visited = [[0]*N for _ in range(N)] # 미로의 크기만큼 생성
    queue = []			# 큐 생성
    queue.append(i,j)	# 시작점 enqueue
	visited[i][j] = 1	# 시작점 방문표시
    while queue: # 큐가 비어있지 않으면 반복
        i, j = queue.pop(0)	# dequeue
        if maze[i][j] == 3:
            return visited[i][j] - 2 # 출발, 도착 칸 제외
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # i, j 인접한 칸에 대해
            ni, nj = i+di, j+dj # 주변 칸 좌표
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                # 주변 칸 좌표가 미로를 벗어나지 않고, 벽이 아니고, 방문한적이 없으면
                queue.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
	return 0 # 도착지를 찾지 못한 경우
    
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = fstart(N)
    ans = bfs(sti, stj, N)
	print(f'#{tc} {ans}')
```

```python
# dfs (재귀)
def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
	return -1, -1 # 못찾으면 -1 리턴

def dfs(i,j,N,c): # 지나온 칸 수
    global minV
    if maze[i][j] == 3: # 목적지에 도착하면 최소거리와 비교
        if minV > c:
            minV = c
    else:
        maze[i][j] = 1
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1:
                dfs(ni,nj,N,c+1)
    	maze[i][j] = 0
    
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = fstart(N)
    minV = 10000
    dfs(sti,stj,N,0)
    if minV == 1000:
        minV = 1
	print(f'#{tc} {minV-1}') # 출발지 제외하고 출력
```

