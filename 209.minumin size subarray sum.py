class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0 # boundary of sliding window
        total = 0
        
        min_subarray_length = 100001
        min_subarray_total = 0

        while r < len(nums):
            total += nums[r]
            while total >= target: 
                min_subarray_length = min(min_subarray_length, r-l+1)
                total -= nums[l]
                l += 1
            r += 1

        if min_subarray_length == 100001: 
            min_subarray_length = 0
        return min_subarray_length

# test case 1
# target = 7, nums = [2,3,1,2,4,3]
# l | r | total |  min_subarray_length 
# 0 | 0 | 0     |
# 0 | 1 | 2
# 0 | 2 | 5
# 0 | 3 | 6
# 0 | 4 | 8
# 0 | 4 | 8.    | 4
# 1 | 4 | 6    | 4
# 1 | 5 | 10 
# 2 | 5 | 7
# 3 | 5 | 6
# 3 | 6 | 9   
# 4 | 6 | 7
# 5 | 6 | 3   | 2
