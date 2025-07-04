class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        
        def dfs(i,j):
            grid[i][j]=0
            for dx,dy in[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if (0<=dx<n and 0<=dy<m )and grid[dx][dy]:
                    dfs(dx,dy)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and(i==0 or i==n-1 or j==0 or j==m-1):
                    dfs(i,j)
        return(sum(sum(row) for row in grid))
