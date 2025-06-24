class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        n,m=len(image),len(image[0])
        original_color=image[sr][sc]
        if original_color == color:
            return image
        
        q = deque([(sr, sc)])           

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        
        while q:
            r,c=q.popleft()

            if image[r][c]==original_color:
                image[r][c]=color
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == original_color:
                        q.append((nr,nc))
        return image