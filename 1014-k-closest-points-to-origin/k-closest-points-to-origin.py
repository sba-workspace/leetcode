import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heappush, heappop = heapq.heappush, heapq.heappop
        
        # Max-heap
        heap = []
        
        for x, y in points:
            distance = x*x + y*y
            heappush(heap, (-distance, (x,y)))
            if len(heap) > k:
                heappop(heap)
                
        ans = []
        for distane, coords in heap:
            ans.append(coords)
        return ans