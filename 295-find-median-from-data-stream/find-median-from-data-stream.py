import bisect

class MedianFinder:

    def __init__(self):
        # We'll store numbers in a sorted list
        self.data = []

    def addNum(self, num: int) -> None:
        # Insert num into the sorted list using binary search
        bisect.insort(self.data, num)

    def findMedian(self) -> float:
        n = len(self.data)
        mid = n // 2
        if n % 2 == 1:
            # Odd length → middle element
            return float(self.data[mid])
        else:
            # Even length → average of two middle elements
            return (self.data[mid - 1] + self.data[mid]) / 2