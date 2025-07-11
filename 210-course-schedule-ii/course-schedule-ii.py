class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res=[]
        
        while q:
            node=q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei]==0:
                    q.append(nei)
        
        if numCourses==len(res):
            return res
        return []