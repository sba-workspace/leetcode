from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = []
        
        for s in range(m + n - 1):
            # Temporary list to store the current diagonal
            temp = []
            
            # Determine the starting row and column based on the sum s
            if s < n:
                row = 0
                col = s
            else:
                row = s - n + 1
                col = n - 1
            
            # Traverse the diagonal
            while row < m and col >= 0:
                temp.append(mat[row][col])
                row += 1
                col -= 1
            
            # If even sum, reverse the collected diagonal
            if s % 2 == 0:
                result.extend(temp[::-1])
            else:
                result.extend(temp)
        
        return result
