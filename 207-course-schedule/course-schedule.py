from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        path = [False] * numCourses

        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(i):
            visited[i] = True
            path[i] = True
            for nei in adj[i]:
                if not visited[nei]:
                    if dfs(nei):
                        return True  # cycle detected
                elif path[nei]:
                    return True  # back edge found (cycle)
            path[i] = False
            return False  # no cycle in this path

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False  # cycle detected, cannot finish all courses

        return True  # no cycles found, all courses can be finished
