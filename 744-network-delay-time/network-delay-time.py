class Solution:
    def __init__(self):
        self.visitedStack = []
        self.VERY_LARGE_NUMBER = 10 ** 6
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        sourceNode = k - 1

        if sourceNode >= n:
            return -1
        
        adjacency_matrix = [
            [(0 if i == j else self.VERY_LARGE_NUMBER) for i in range(n)]
            for j in range(n)
        ]

        self.visitedStack = [False for i in range(n)]

        for edge in times:
            u, v, weight = edge
            x, y = u - 1, v - 1
            adjacency_matrix[x][y] = weight
        
        # relaxing the edges
        for i in range(len(adjacency_matrix)):
            for source in range(len(adjacency_matrix)):
                if source == i:
                    continue
                for dest in range(len(adjacency_matrix)):
                    if dest == i:
                        continue
                    if source == dest:
                        continue
                    dist = adjacency_matrix[source][i] + adjacency_matrix[i][dest]
                    if dist < adjacency_matrix[source][dest]:
                        adjacency_matrix[source][dest] = dist
        
        result = max(adjacency_matrix[sourceNode])
        return (-1 if result == self.VERY_LARGE_NUMBER else result)