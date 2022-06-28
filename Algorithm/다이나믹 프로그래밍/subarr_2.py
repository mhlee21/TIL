import sys
def maxSebArray(nums):
    best_sum = -sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum+num)
        # 단계마다 최댓값을 저장
        best_sum = max(best_sum, current_sum)
    return best_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSebArray(arr))