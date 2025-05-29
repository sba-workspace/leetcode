class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n & (n-1)==0)
        
        # Any power of two has exactly one bit set in its binary representation. 
        #8 is 1000 and 16 is 10000. 
        #If you subtract 1 from such numbers, all bits to the right of the set bit become 1, 
        # and a bitwise AND will result in zero.