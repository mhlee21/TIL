---
title: sort
date: 2022-02-22 13:45:53
categories: 
- algorithm
tags:
- algorithm
- 빅-오 표기법
- Bubble sort
- Counting sort
- Selection sort
- Insertion sort
---

# 빅-오 표기법

* 알고리즘의 작업량을 표현할 때 시간 복잡도를 이용한다.

* 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n 에 대한 항만을 표시
* 계수는 생략하여 표시

![image-20220209110253514](image-20220209110253514.png)

# Bubble sort

인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.

# Counting sort

항목들의 순서를 결정하기 위해 집합에 각 항목이 몇개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

# Selection sort

주어진 리스트중에 최소값을 찾아 그 값을 맨 앞에 위치한 값과 교체한다.

맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.

# Insertion sort

