class Solution:
    def minimumOperations(self, a: List[int]) -> int:
        return next(i for i in count() if len(b:=a[i*3:])==len({*b}))