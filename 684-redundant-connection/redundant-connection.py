class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        return (t:=''.join(map(chr,range(1001)))) and next([u,v] for u,v in e if (t[u]==t[v],t:=t.replace(t[u],t[v]))[0])