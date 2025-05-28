class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stoneSet=set(stones)
        stoneMap={stone:set() for stone in stones}
        stoneMap[0].add(0)

        for stone in stones:
            for k in stoneMap[stone]:
                for jump in [k-1,k,k+1]:
                    if jump>0 and(stone+jump) in stoneSet:
                        stoneMap[stone+jump].add(jump)
        return len(stoneMap[stones[-1]])>0