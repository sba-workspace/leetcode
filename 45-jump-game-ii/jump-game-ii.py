from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        #bruteforce
        n = len(nums)
        visited = [False] * n
        queue = deque([(0, 0)])  # (current_index, jumps)

        while queue:
            index, jumps = queue.popleft()
            
            if index == n - 1:
                return jumps
            
            max_jump = nums[index]
            for next_index in range(index + 1, min(n, index + max_jump + 1)):
                if not visited[next_index]:
                    visited[next_index] = True
                    queue.append((next_index, jumps + 1))

        