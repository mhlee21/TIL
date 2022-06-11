---
title: 퀵정렬(Quick sort)
toc: true
date: 2022-03-31 16:01:43
categories:
- algorithm
tags:
- algorithm
- quick sort
- sort
---

# Quick sort

pivot 을 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치 시킨다.

```python
def quicksort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end) # 확정된 피봇 위치를 기준으로
        quicksort(a, begin, p-1) # 왼쪽 구간에 대해 퀵 정렬을 다시 수행한다.
        quicksort(a, p+1, end) # 오른쪽 구간에 대해 퀵 정렬을 다시 수행한다.
```

* 알고리즘 기법 : 분할 정복
* 최악의 경우 O(N^2) 지만, 평균적으로는 가장 빠르다. O(nlogn)
* 분할 방법에 따라 Hoare(호어), Lomuto(로무토) 방법이 존재한다.
* Hoare 방식이 더 유리하다. 평균적으로 swap을 3배 이상 덜 발생시키기 때문이다.

> 1. 피봇 값보다 큰 값들은 오른쪽, 작은 값들은 왼쪽 집합에 위치시킴
>
> 2. 피봇 값을 두 집합의 가운데에 위치시킴
>
>    2 과정을 거친 피봇 값은 다음 정렬 과정에서 제외되며, 피봇값이 위치한 곳은 정렬된 상태일 대 자기가 있어야 할 위치에 놓임

## Hoare-Partition 알고리즘

![image-20220331164829296](image-20220331164829296.png)

```python
def partition(a, begin, end):
    pivot = arr[begin]
    i = begin
    j = end
    while i<=j:
        while i <= j and a[i] <= pivot: i += 1
        while i <= j and a[j] >= pivot: j -= 1
        if i<j:
            a[i], a[j] = a[j], a[i]
    a[begin], arr[j] = arr[j], arr[begin]
    return j
```

## Lomuto-partition 알고리즘

![image-20220331164837560](image-20220331164837560.png)

```python
def partition(a, begin, end):
    pivot = a[end]
    i = begin - 1;
    for j in range(begin,end):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    pivotIdx = i+1
    a[pivotIdx], a[end] = a[end], a[pivotIdx]
    return pivotIdx
```

