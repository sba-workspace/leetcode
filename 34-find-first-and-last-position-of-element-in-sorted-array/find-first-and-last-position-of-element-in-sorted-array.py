class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearch(nums,target,isSearchingLeft):
            l=0
            h=len(nums)-1
            idx=-1
            while l<=h:
                mid=(l+h)//2

                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    h=mid-1
                else:
                    idx=mid
                    if isSearchingLeft:
                        h=mid-1
                    else:
                        l=mid+1
            return idx
        left=binarysearch(nums,target,True)
        right=binarysearch(nums,target,False)

        return [left,right]

