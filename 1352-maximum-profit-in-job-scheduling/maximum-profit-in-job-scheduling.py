class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        startTime.sort()

        @cache
        def dp(i: int) -> int:
            if i >= n: return 0
            
            j = bisect.bisect_left(startTime, jobs[i][1])
            return max(dp(i + 1), dp(j) + jobs[i][2])

        return dp(0)