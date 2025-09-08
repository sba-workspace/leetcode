class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        op = 0
        # Split into k groups, and compute the number of operations for each group length. 
        for i in range(k):
            seq = []
            j = i
            while j < n:
                seq.append(arr[j])
                j += k
            #Check LNDS
            lnds = []

            for num in seq:
                idx = bisect.bisect_right(lnds, num)
                if idx == len(lnds):
                    lnds.append(num)
                else:
                    lnds[idx] = num
            op += len(seq) - len(lnds) 
        return op