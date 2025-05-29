class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        first=m-1
        sec=n-1
        right=m+n-1

        while sec>=0:
            if first>=0 and nums1[first]>nums2[sec]:
                nums1[right]=nums1[first]
                first-=1
            else:
                nums1[right]=nums2[sec]
                sec-=1
            right-=1
