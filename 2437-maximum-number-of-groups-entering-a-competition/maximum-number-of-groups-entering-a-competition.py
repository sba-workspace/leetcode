class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        grades.sort()
        
        groups, size, used = 0, 1, 0
        while used + size <= n:
            used += size
            groups += 1
            size += 1
        return groups