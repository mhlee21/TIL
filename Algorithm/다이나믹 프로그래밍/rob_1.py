def rob(nums):
    def _rob(i):
        if i<0:
            return 0
        return max(_rob(i-1), _rob(i-2)+nums[i])
    return _rob(len(nums)-1)

arr = [2,7,9,3,1]
print(rob(arr))