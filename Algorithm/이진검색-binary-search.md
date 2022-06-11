---
title: 이진검색(binary search)
toc: true
date: 2022-03-30 11:20:26
categories:
- algorithm
tags:
- algorithm
- 이진검색
---

# 이진 검색

자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

- 목적 키를 찾을 때 까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여나가면서 보다 빠르게 검색을 수행함

>  💡 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

## 검색 과정

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.

## 알고리즘 : 반복구조

```python
def binary_search(n,s,k):
  low = 0
  high = n-1
  while low <= high:
    mid = low + (high - low)//2
    if s[mid] == k:
      return mid
    elif s[mid] > k:
      high = mid-1
    else:
      low = mid+1
  return -1

arr = [2,4,7,9,11,19,23]
res = binary_search(len(arr),arr,11)
print(f'[{res}] {arr[res]}')
```

```bash
[4] 11
```



## 알고리즘 : 재귀구조

```python
def binary_search(s,low,high,key):
  if low > high:
    return -1
  else:
    mid = (low+high)//2
    if key == s[mid]:
      return mid
    elif key < s[mid]:
      return binary_search(s,low,mid-1,key)
    else:
      return binary_search(s,mid+1,high,key)

arr = [2,4,7,9,11,19,23]
res = binary_search(arr,0,len(arr),4)
print(f'[{res}] {arr[res]}')
```

```bash
[1] 4
```

