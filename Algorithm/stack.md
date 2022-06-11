---
title: stack
date: 2022-02-22 09:42:08
categories: 
- algorithm
tags: 
- algorithm
- stack
- memoization
- DP
- DFS
- 계산기
- 백트래킹
---

# 스택

* 물건을 쌓아 올린듯, **자료를 쌓아 올린** 형태의 자료구조
* **LIFO (Last-In-First-Out, 후입선출)** : 가장 마지막에 들어간 것이, 가장 처음에 나온다.
* 가장 위에서만 데이터의 삽입&삭제가 일어난다.
* 스택의 연산 (메서드)
  * createstack : 스택을 생성하는 연산, size 필요
  * isempty : 스택이 현재 비어있는지를 확인, true/false 리턴
  * isfull : 스택이 현재 꽉 차있는지를 확인, true/false 리턴
  * push : 스택에 새로운 데이터 요소를 삽입하는 연산
  * pop : 스택에서 가장 위에 있는 요소를 제거하는 연산, 데이터 반환
  * peek : 스택에서 가장 위에 있는 요소를 반환하는 연산 (데이터를 확인하고 싶은 경우)
* 스택의 데이터 구조
  * top : 스택의 가장 위에 있는 위치를 저장하고 있는 데이터
  * size : 스택의 크기를 저장하고 잇는 데이터
  * items : 스택에 담길 데이터를 저장

## 스택의 삽입/삭제 과정

* push
  1. top을 증가시킴
  2. top이 가리키는 자리에 원소를 저장
* pop
  1. 원소를 반환함
  2. top 을 감소시킴

## 스택의 응용 1: 괄호 검사

* 조건
  1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
  2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
  3. 괄호 사이에는 포함 관계만 존재한다.

* 문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 삽입, 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지를 검사한다.
* 이때, 스택이 비어있으면 조건 1 또는 조건 2에 위배되고, 짝이 맞지 않으면 조건 3에 위배된다.
* 마지막 괄호까지 조사한 후에도 스택에 괄호가 남아있으면 조건 1에 위배된다.

## 스택의 응용 2 : function call

* 프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리
  * 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임(stack frame) 에 저장하여 시스템 스택에 삽입
  * 함수의 실행이 끝나면 시스템 스택의 top 원소를 삭제(pop)하면서 프레임에 저장되어있던 복귀주소를 확인하고 복귀
  * 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

![image-20220221144726902](image-20220221144726902.png)

<br/><br/>

# 재귀호출

* 자기 자신을 호출하여 순환 수행되는 것
* 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출 방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성

![image-20220221144953508](image-20220221144953508.png)

 <br/><br/>

# Memoization & DP

## Memoization

* **이전에 계산한 값을 메모리에 저장**해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
* 💡동적 계획법의 핵심

```python
# memo 를 위한 배열을 할당하고, 모두 0으로 초기화
# memo[0]을 0으로 memo[1]는 1로 초기화 한다.

memo = [0,1]
def fibo1(n):
    global memo
    if n >= 2 and len(memo) < n:
        memo.append(fifo1(n-1) + fifo(n-2))
       return memo[n]
```

## DP (Dynamic Programming)

* 동적 계획 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.
* Memoization 과의 차이점
  * Memoization은 함수의 실행 결과를 저장하는 것이라면, DP는 이전 값을 이용해 다음 값을 얻을 수 있다.
  * 중복계산을 피하기 위해 계산결과를 저장해두는 Memoization을 사용할 수 있다.
* 분할 정복 과의 차이점
  * 분할 정복도 큰 문제를 작은 문제로 나누어 푸는 것이 동적 계획법과 같지만, 계산한 부분문제를 한번만 사용하고 더이상 쓰지 않는다.

* 먼저 입력 크기가 작은 부분문제들을 모두 해결한 후에, 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.
  1) 문제를 부분 문제로 분할한다.
  2) 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분문제부터 해를 구한다.
  3) 그 결과는 테이블에 저장하고, 테이블에 저장된 부분문제의 해를 이용하여 상위 문제의 해를 구한다.

```python
def fibo2(n):
    f = [0,1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]
```

### DP의 구현 방식

* recursive 방식 : fibo1()
* iterative 방식 : fibo2()
* memoization 을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능면에서 보다 효율적이다.
  * 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문이다.

<br/><br/>

# DFS

* 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요

* 두가지 방법

  * 너비 우선 탐색 (Breadth First Search, BFS)
  * 깊이 우선 탐색 (Depth First Search, DFS)
    * 재귀를 이용해서 구현
    * 반복을 이용해서 구현 - stack 사용

* 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

  1) 시작 정점 v를 결정하여 방문한다.

  2) 정점 v에 인접한 정점 중에서

     * 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push 하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2를 반복한다.

     * 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해 스택을 pop 하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2를 반복한다.

  3. 스택이 공백이 될 때 까지 2를 반복한다.

```python
visited[], stack[] 초기화
DFS(v)
	v 방문;
    visited[v] <- true;
    do {
        if (v의 인접 정점 중 방문 안한 w 찾기)
        	push(v);
        	while(w){
                w 방문;
                visited[w] <- true;
                push(w);
                v <- w;
                v의 인접 정점 중 방문 안한 w 찾기
            }
        v <- pop(stack);
    } while(v)
```

<br/><br/>

# 스택의 응용

## 계산기

* 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.

* 중위 표기법(Infix notation)을 후위 표기법(Postfix notation) 으로 변환하는 방법

  1. '('를 만나면 스택에 push 한다.

  2. ')'를 만나면 스택에서 '(' 가 나올때 까지 pop 하여 출력하고, '(' 는 pop하여 버린다.
  3. 연산자를 만나면 스택에서 그 연산자보다 낮은 우선순위의 연산자를 만날 때 까지 pop 하여 출력한 뒤에 자신을 push 한다.
  4. 피 연산자는 그냥 출력한다.
  5. 모든 입력이 끝나면 스택에 있는 연산자들을 모두 pop 하여 출력한다.

* 후위 표기법 수식의 계산

  1. 숫자를 만나면 숫자는 스택에 push한다.

  2. 연산자를 만나면 스택에서 pop을 두번 하여 그 두 데이터를 가지고 연산한 다음 결과를 스택에 push 한다.

## 백트래킹

* 해를 찾는 도중에 '막히면' (즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법
* 최적화(optimization) 문제와 결정(decision) 문제를 해결할 수 있다.
* 결정문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no' 로 답하는 문제

| 문제                      | url                                  |
| ------------------------- | ------------------------------------ |
| 미로찾기                  | https://www.acmicpc.net/problem/2178 |
| n-Queen                   | https://www.acmicpc.net/problem/9663 |
| Map coloring              |                                      |
| 부분집합의 합(Subset Sum) | https://www.acmicpc.net/problem/1182 |

* 백트래킹과 DFS의 차이
  * 깊이 우선 탐색이 모든 경로를 추적하는데 비해, 백트래킹은 불필요한 경로를 조기에 차단
  * Pruning (가지치기) : 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임



[ 일반 백트래킹 알고리즘]

```python
def checknode(v):
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)
```



[부분집합 구하기]

```pyhon
def backtrack(a,k,input):
	global MAXCANDIDATES
	c = [0] * MAXCANDIDATES
	
	if k == input:
		process_solution(a,k) # 답이면 원하는 작업을 한다.
	else:
		k += 1
		ncandidates = construct_candidates(a,k,input,c)
		for i in range(ncandidates):
            a[k] = c[i]
            
            backtrack(a,k,input)
		
def construct_candidates(a,k,input,c):
	c[0] = True
	c[1] = False
	return 2
	
MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
backtrack(a,0,3)
```

