class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hash={5:0,10:0}

        for bill in bills:
            if bill == 5:
                hash[5]+=1
            elif bill==10:
                if hash[5]>=1:
                    hash[10]+=1
                    hash[5]-=1
                else:
                    return False
            else:
                if hash[10]>=1 and hash[5]>=1:
                    hash[10]-=1
                    hash[5]-=1
                elif hash[5]>=3:
                    hash[5]-=3
                else:
                    return False
        return True
