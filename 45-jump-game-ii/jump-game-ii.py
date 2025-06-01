from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0#(region of jumps):[2,3,1,1,4]
        n=len(nums)             # _ | __ | __
        end,far=0,0             # 0   1    2
        
        for i in range(n-1):
            far=max(far,i+nums[i])

            if i==end:
                jumps+=1
                end=far
        return jumps