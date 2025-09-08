class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        prune = lambda x: (x in (2,3) or x%6 in (1,5)) and x > 1  # prunes a list of possible primes
        isPrime = lambda x: all(x % posPrime for posPrime         # boolean function returns whether a prime
                             in filter(prune,range(isqrt(x)+1)))  
        
        n = len(nums)

        cands = sorted(filter(prune,                              # collect the diagonal elements of the array,
                         {nums[i][i   ] for i in range(n)}|       # then prune and sort the list, and sort the  
                         {nums[i][-i-1] for i in range(n)})       # pruned list, reverse = True.
                      ,reverse = True)                          

        for c in cands:                                           # determine the first element in the sorted list
            if isPrime(c): return c                               # that is prime
        return 0 