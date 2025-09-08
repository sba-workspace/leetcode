class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = 0
                    stack = [(i,j)]
                    grid[i][j] = 0
                    while stack:
                        x, y = stack.pop()
                        cnt += 1
                        if x > 0 and grid[x-1][y] == 1:
                            grid[x-1][y] = 0
                            stack.append((x-1,y))
                        if x+1 < m and grid[x+1][y] == 1:
                            grid[x+1][y] = 0
                            stack.append((x+1,y))
                        if y > 0 and grid[x][y-1] == 1:
                            grid[x][y-1] = 0
                            stack.append((x,y-1))
                        if y+1 < n and grid[x][y+1] == 1:
                            grid[x][y+1] = 0
                            stack.append((x,y+1))
                    ans = max(ans, cnt)
        return ans