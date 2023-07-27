class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insert_idx] = nums[i]
                insert_idx += 1
        return insert_idx
            