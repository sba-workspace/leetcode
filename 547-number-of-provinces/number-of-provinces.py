class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        parent=list(range(n))

        def find(p):
            root=p
            while root!=parent[root]:
                parent[root]=parent[parent[root]]
                root=parent[root]

            return root
        def union(u,v):
            root1,root2=find(u),find(v)

            if root1!=root2:
                parent[root2]=root1

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    union(i,j)
        provinces = len(set(find(i) for i in range(n)))
        return provinces