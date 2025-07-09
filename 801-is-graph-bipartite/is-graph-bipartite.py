class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[0]*len(graph) #1-odd 2-even

        def bfs(i):
            if color[i]:
                return True
            q=deque([i])
            color[i]=1

            while q:
                node=q.popleft()
                for nei in graph[node]:
                    if color[node]==color[nei]:
                        return False
                    elif color[nei]==0:
                        color[nei]=-color[node]
                        q.append(nei)
                        
            return True



        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True