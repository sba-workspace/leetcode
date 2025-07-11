class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        safe={}

        def safe_node_dfs(i):
            if i in safe:
                return safe[i]
            safe[i]=False

            for nei in graph[i]:
                if not safe_node_dfs(nei):
                    return safe[i] #False
            safe[i]=True
            return safe[i] #True

        res=[]
        for i in range(n):
            if safe_node_dfs(i):
                res.append(i)
        return res