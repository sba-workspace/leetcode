class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m=len(board),len(board[0])
        temp="s"
        q=deque()

        for i in range(n):
            if board[i][0]=="O":
                q.append((i,0))
            if board[i][m-1]=="O":
                q.append((i,m-1))
        for j in range(m):
            if board[0][j]=="O":
                q.append((0,j))
            if board[n-1][j]=="O":
                q.append((n-1,j))
        
        while q:
            i,j=q.popleft()
            board[i][j]="S"
            for ii,jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not((0 <= ii < n) and (0 <= jj < m)):
                    continue
                if board[ii][jj]!="O":
                    continue
                q.append((ii,jj))
                board[ii][jj]="S"
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = "O"
        