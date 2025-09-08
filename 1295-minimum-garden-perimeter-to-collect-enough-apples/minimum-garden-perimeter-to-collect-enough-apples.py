class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        
        return 8*bisect_left(list(range(65536)),
                 neededApples, key = lambda x: x*(x*(4*x+6)+2))