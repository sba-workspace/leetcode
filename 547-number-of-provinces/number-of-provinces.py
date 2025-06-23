class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        cnt=0

        def bfs(city):
            q=deque([city])
            while q:
                node=q.popleft()
                for neighbor in range(n):
                    if isConnected[node][neighbor] and not visited[neighbor]:
                        visited[neighbor]=True
                        q.append(neighbor)
        for city in range(n):
            if not visited[city]:
                visited[city]=True
                bfs(city)
                cnt+=1
        return cnt