class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        lst=[]
        def sub(i,s1,sum1,last):
            if i>=len(num):
                if sum1==target:
                    lst.append(s1)
                return
            for j in range(i,len(num)):
                if j>i and num[i]=="0":
                    return
                curr=int(num[i:j+1])
                if i==0:
                    sub(j+1,s1+str(curr),curr,curr)
                else:
                    sub(j+1,s1+"+"+str(curr),sum1+curr,curr)
                    sub(j+1,s1+"-"+str(curr),sum1-curr,-curr)
                    sub(j+1,s1+"*"+str(curr),sum1-last+(curr*last),curr*last)
        s1=""
        sub(0,s1,0,0)
        return lst
            