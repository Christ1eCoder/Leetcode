class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) -1
        res = [0 for i in range(len(nums))]
        i = 0
        while left <= right: 
            if left == right: 
                res[len(nums)-1-i] = nums[right]**2
                break

            left_abs = nums[left]**2
            right_abs = nums[right]**2
            if left_abs < right_abs: 
                res[len(nums)-1-i] = right_abs
                right -= 1
                i += 1
            elif left_abs > right_abs: 
                res[len(nums)-1-i] = left_abs
                left += 1
                i += 1
            else: 
                res[len(nums)-1-i] = right_abs
                res[len(nums)-1-i-1] = left_abs
                right -= 1
                left += 1
                i += 2
        return res

# test case 1 nums = [-4,-1,0,3,10]
# res = [0, 0, 0, 0, 100]


            
