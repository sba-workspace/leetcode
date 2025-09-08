class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        l = len(nums)
        s = 0
        for i in range(0, l - 1):
            s += abs(nums[i] - nums[i + 1])

        def helper(ar):
            if len(ar) < 4:
                return 0
            mn_max = min(ar[-1], ar[-2])
            ans = 0
            for i in range(l - 4, -1, -1):
                cur_max = max(ar[i], ar[i + 1])
                ans = max(ans, 2 * (mn_max - cur_max))
                mn_max = max(mn_max, min(ar[i + 1], ar[i + 2]))
            for i in range(1, l - 1):
                initial_score = abs(ar[i] - ar[i + 1])
                change_score = abs(ar[i + 1] - ar[0])
                ans = max(ans, change_score - initial_score)
            return ans
        
        mx = max(helper(nums), helper(nums[::-1]))
        return s + mx      