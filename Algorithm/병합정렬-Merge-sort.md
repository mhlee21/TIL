---
title: 병합정렬(Merge sort)
toc: true
date: 2022-03-31 20:46:02
categories: 
- algorithm
tags:
- algorithm
- Merge sort
- sort
---

# Merge sort (병합정렬)

여러개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

* 시간복잡도 : O(n log n)

## 분할 단계

![image-20220331204815871](image-20220331204815871.png)

## 병합 단계

![image-20220331204835149](image-20220331204835149.png)

```python
def merge_sort(arr):
  if len(arr) == 1:
    return arr

  # 분할 과정
  mid = len(arr)//2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  
  # 병합 과정
  merged_arr = []
  l = h = 0
  while l < len(left) and h < len(right):
    if left[l] < right[h]:
      merged_arr.append(left[l])
      l += 1
    else:
      merged_arr.append(right[l])
      h += 1
  merged_arr += left[l:]
  merged_arr += right[h:]
  return merged_arr

arr = [69,10,30,2,16,8,31,22]
print(merge_sort(arr))
```

```bash
[2, 16, 10, 22, 22, 30, 31, 69]
```

