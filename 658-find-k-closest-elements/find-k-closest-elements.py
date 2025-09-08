class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            diff = abs(x - num)
            # Use max heap so we keep only the smallest differences (we pop the largest differences)
            heapq.heappush(heap, (-diff, -num))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for diff, num in heap:
            ans.append(-num)

        return sorted(ans)
        