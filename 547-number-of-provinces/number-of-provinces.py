class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        cnt=0

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] and not visited[neighbor]:
                    visited[neighbor]=True
                    dfs(neighbor)
        for city in range(n):
            if not visited[city]:
                visited[city]=True
                dfs(city)
                cnt+=1
        return cnt