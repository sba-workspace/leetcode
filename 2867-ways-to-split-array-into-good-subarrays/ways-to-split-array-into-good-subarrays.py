class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:       
        last_idx = -1
        ans = 1
        mod = 1_000_000_007

        for i in range(len(nums)):
            if last_idx == -1 and nums[i] == 1:
                last_idx = i
            elif last_idx != -1 and nums[i] == 1:
                ans = (ans * (i - last_idx)) % mod
                last_idx = i
        
        return ans if last_idx != -1 else 0