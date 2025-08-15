from typing import List
import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def generate_subset_sums(arr):
            sums = [0]
            for x in arr:
                sums += [s + x for s in sums]
            return sorted(set(sums))
        
        n = len(nums)
        left, right = nums[:n//2], nums[n//2:]
        left_sums = generate_subset_sums(left)
        right_sums = generate_subset_sums(right)
        
        best = float('inf')
        for s1 in left_sums:
            rem = goal - s1
            # Find closest value to rem in right_sums
            i = bisect.bisect_left(right_sums, rem)
            for j in [i-1, i, i+1]:
                if 0 <= j < len(right_sums):
                    total = s1 + right_sums[j]
                    best = min(best, abs(total - goal))
        return best