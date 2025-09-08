class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n=len(temps)
        ans=[0]*n
        stk=[]
        for i in range(n-1,-1,-1):
            while stk and temps[stk[-1]]<=temps[i]:
                stk.pop()

            if stk:
                ans[i]=stk[-1]-i
            stk.append(i)
        return ans


