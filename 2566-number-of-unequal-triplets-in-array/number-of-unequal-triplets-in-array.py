
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counts = Counter(nums)
        result = 0
        left = 0
        for num in counts.keys():
            right = len(nums) - counts[num] - left
            result += left * counts[num] * right
            left += counts[num]
        return result