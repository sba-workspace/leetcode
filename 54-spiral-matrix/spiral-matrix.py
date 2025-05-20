class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])

        ans=[0]*(m*n)
        idx=0
        
        left=top=0
        right=n-1
        bottom=m-1
        dir=0 #L-->R(0),T-->B(1),R-->L(2),B-->T(3) 

        while(left<=right and top<=bottom):
            if(dir==0):
                for j in range(left,right+1):
                    ans[idx]=matrix[top][j]
                    idx+=1
                top+=1
                dir=1
            elif (dir==1):
                for i in range(top,bottom+1):
                    ans[idx]=matrix[i][right]
                    idx+=1
                right-=1
                dir=2
            elif(dir==2):
                for j in range(right,left-1,-1):
                    ans[idx]=matrix[bottom][j]
                    idx+=1
                bottom-=1
                dir=3
            else:
                for i in range(bottom,top-1,-1):
                    ans[idx]=matrix[i][left]
                    idx+=1
                left+=1
                dir=0
        return ans