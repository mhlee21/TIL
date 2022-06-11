---
title: queue>구현
date: 2022-02-25 14:02:32
categories: 
- algorithm
tags:
- algorithm
- queue
---

# Queue 구현

## 1. list

```python
"""
문제1. 기본 Queue 구현 - 기본 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""

#1. Queue 생성
queue = []
#2. Queue에 데이터를 삽입
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue)
```

```bash
[1, 2, 3]
1
2
3
[]
```


## 2. funtion

```python
"""
1) 기본 개념
선형 큐 기본
- 큐의 크기 == 배열의 크기
- front: 마지막에 꺼내진 원소의 인덱스
- rear: 저장된 마지막 원소의 인덱스

초기 상태
front, rear = -1, -1

공백 상태
 - front = rear

포화 상태
 - Queue가 전부 찼을 때
 - rear = n - 1 (n: 배열의 크기, n-1: 배열의 마지막 인덱스)

2) 기본 Queue의 연산 과정
1. 공백 Queue 생성
    - 고정 배열에서 Queue의 사이즈를 지정
    - front와 rear의 값을 -1로 초기화
        - 이때 파이썬에서 음수 인덱스 유의
2. 원소 A 삽입
    삽입 과정은 rear의 증가
    - front → -1
    - rear → 0 (+1)
3. 원소 B 삽입
    삽입 과정은 rear의 증가
    - front → -1
    - rear → 1 (+1)
4. 원소 반환/삭제
    삭제 과정은 front의 증가
    - front → 0 (+1)
        - 이때 해당 자리에 있었던 원소 반환
    - rear → 1
5. 원소 C 삽입
    - front → 0
    - rear → 2 (+1)
6. 원소 반환/삭제
    - front → 1 (+1)
    - rear → 2
7. 원소 반환/삭제
    - front → 2 (+1)
    - rear → 2
    - front와 rear가 같아진다? → 공백 상태
"""

"""
문제2. 고정 배열 크기의 Queue 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""

# Queue의 사이즈 지정 - createQueue
# 고정 크기의 배열로 Queue를 생성하는 것이 상대적으로 가변 배열(리스트)보다 빠르다.
SIZE = 4
Q = [0] * SIZE

# 초기 상태의 표현
front, rear = -1, -1

# isFull
def is_full():
    """
    Queue가 포화상태인지 확인
    - 리스트에서는 큰 문제가 되지 않지만 고정 배열의 경우 확인 필요
    """

    # global 키워드를 사용하는 이유? -> https://stackoverflow.com/questions/1261875/python-nonlocal-statement
    # 단순 '참조'만 하는 것이면 LEGB Rule에 따라 전역 영역의 변수를 참조
    # 하지만 함수 내부에서 특정 값을 '참조'하고 & '변경'하기 위해서는 global 키워드 사용하여 전역에 있는 변수를 로컬 변수처럼 활용
    global rear
    return rear == len(Q) - 1

# isEmpty
def is_empty():
    """
    Queue가 공백상태인지 확인
    """
    global front, rear
    return front == rear

# enQueue
def enqueue(item):
    """
    Queue의 뒤쪽(rear 다음)에 원소를 삽입
    - rear를 뒤쪽으로 옮기고 (rear + 1)그 자리에 원소를 삽입
    - Stack의 top을 옮겨놓고 그 자리에 요소를 넣었던 것을 떠올리자
    """
    global rear
    if is_full():
        print("Queue is full!")
    else:
        rear += 1
        Q[rear] = item

# deQueue
def dequeue():
    """
    Queue의 앞쪽(front)에서 원소를 삭제하고 반환
    - front를 뒤쪽으로 옮기고(front + 1) 그 자리에 있는 원소를 반환하며 삭제
    """
    global front
    if is_empty():
        return "Queue is empty!"
    else:
        front += 1
        return Q[front]

# Qpeek
def Qpeek():
    """
    Queue의 앞쪽(front)의 한 자리뒤(front+1)에서 원소를 삭제없이 반환
    - front의 값을 단순하게 증가시켜 가져온다. (큐의 첫 번째 원소 반환)
    - 이때 중요한 것은 dequeue와 다르게 front의 값 자체를 '변경'하지 않는다는 점
     - front += 1은  front + 1과 다르다.
     - dequeue와 비교하며 생각
    """
    global front, rear
    if is_empty():
        print("Queue is empty!")
    else:
        return Q[front + 1]

#1. Queue 초기화 상태 확인
print(Q)

#2. Queue가 비었는지 확인
print(is_empty()) # True

#3. enQueue 작업 & 확인
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5) # Queue is full!

print(Q)

#4. Qpeek
print(Qpeek())

#5. deQueue 작업 & 확인
print(dequeue()) # 1
print(dequeue()) # 2
print(dequeue()) # 3
print(dequeue()) # 4
print(dequeue()) # Queue is empty!
```

```bash
[0, 0, 0, 0]
True
Queue is full!
[1, 2, 3, 4]
1
1
2
3
4
Queue is empty!
```

## 3. class

```python
"""
문제 3. 기본 Queue 구현 - 클래스 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""

class Queue:
    # 생성자 함수
    def __init__(self, size):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        인스턴스 변수 생성
        """
        self.size = size
        self.front = -1
        self.rear = -1
        self.items = [None] * size

    # isEmpty
    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        return self.front == self.rear
    
    # isFull
    def is_full(self):
        """
        Queue에 데이터가 가득 저장되어 있는지 True / False 로 반환
        """
        return self.rear == self.size - 1

    # enQueue 
    def enqueue(self, item):
        """
        Queue에 원소 삽입
        """
        if self.is_full():
            # print("Queue is full!")
            raise Exception("Queue is full!")
        else:
            self.rear += 1
            self.items[self.rear] = item

    # deQueue
    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        if self.is_empty():
            return "Queue is empty!"
        else:
            self.front += 1
            return self.items[self.front]
    
    def Qpeek(self):
        """
        Queue에서 바로 다음에 나올 값 확인
        """
        if self.is_empty():
            # return "Queue is empty!"
            raise Exception("Queue is empty!")
        else:
            return self.items[self.front + 1]

    # length
    def __len__(self):
        """
        Queue의 길이 반환 (들어있는 데이터 개수)
        """
        return self.rear - self.front


#1. queue 인스턴스 생성 size 는 5
Q = Queue(5)
#2. queue가 비었는지 확인
print(Q.is_empty())
#3. 1, 2, 3 원소를 queue에 삽입
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
#4. 원소가 정상적으로 삽입되었는지 확인 / 길이 확인 / 비었는지 여부 확인
print(Q)
print(len(Q))
print(Q.is_empty())
#5. queue에서 원소 삭제 후 반환 & 원소 확인 / 길이 확인
item = Q.dequeue()
print(item)
print(len(Q))
#6. queue가 가득차도록 값 추가
Q.enqueue(4)
Q.enqueue(5)
print(Q.is_full())
#7. 가득 차 있는 상태에서 값 추가
# Q.enqueue(6)
```

```bash
True
<__main__.Queue object at 0x0000018C31218FD0>
3
False
1
2
True
```

## 4. import

```python
"""
문제 4. 기본 Queue 구현 - 기본 구현 (내장 모듈 활용)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""
import queue
#1. Queue 생성
q = queue.Queue()
print(q.empty())
#2. Queue에 데이터를 삽입
q.put(1)
q.put(2)
q.put(3)
print(q.empty())
print(q.full())
print(q.qsize())
#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
print(q.get())
print(q.get())
print(q.get())
print(q.empty())
```

```bash
True
False
False
3
1
2
3
True
```
