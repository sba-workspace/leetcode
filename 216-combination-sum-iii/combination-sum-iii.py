class Solution:
    
    def combinationSum3(self, k: int, n: int):
        res = []

        def dfs(start, size, target, path, total):
            if len(path) == size and total == target:
                res.append(path[:])
                return
            if len(path) >= size or total > target:
                return
            for i in range(start, 10):
                path.append(i)
                dfs(i + 1, size, target, path, total + i)
                path.pop()

        dfs(1, k, n, [], 0)
        return res