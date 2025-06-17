class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        inserted =False
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                if not inserted:
                    res.append(newInterval)
                    inserted=True
                res.append(intervals[i])
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        if not inserted:
            res.append(newInterval)

        return res