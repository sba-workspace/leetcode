class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy
        #tc-O(n) sc-O(1)

        n=len(nums)

        target=n-1

        for i in range(n-2,-1,-1):

            max_jump=nums[i]
            
            if(i+max_jump)>=target:
                target=i

        return target==0