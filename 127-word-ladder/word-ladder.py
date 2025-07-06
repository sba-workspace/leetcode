from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        wordList.append(beginWord)

        # build pattern to word map
        nei = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)

        # Bidirectional BFS
        beginSet = set([beginWord])
        endSet = set([endWord])
        visited = set([beginWord, endWord])
        steps = 1

        while beginSet and endSet:
            # Always expand smaller frontier for efficiency
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            nextSet = set()
            for word in beginSet:
                for i in range(L):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neiWord in nei[pattern]:
                        if neiWord in endSet:
                            return steps + 1
                        if neiWord not in visited:
                            visited.add(neiWord)
                            nextSet.add(neiWord)
            beginSet = nextSet
            steps += 1

        return 0
