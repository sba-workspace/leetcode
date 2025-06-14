class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        cn=[1]*n

        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                cn[i]=cn[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1] and cn[i] <= cn[i+1]:
                 cn[i] = cn[i + 1] + 1
        return sum(cn)