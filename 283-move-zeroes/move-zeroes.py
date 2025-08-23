class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0  
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[lastNonZero], nums[fast] = nums[fast], nums[lastNonZero]
                lastNonZero += 1
        