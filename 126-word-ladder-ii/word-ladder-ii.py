from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        nei = defaultdict(list)
        wordSet = set(wordList)
        wordSet.add(beginWord)
        L = len(beginWord)

        for word in wordSet:
            for i in range(L):
                nei[word[:i] + '*' + word[i+1:]].append(word)

        parents = defaultdict(list)
        q = deque([beginWord])
        visited = set([beginWord])
        found = False

        while q and not found:
            levelVisited = set()
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    found = True
                for i in range(L):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            if neiWord not in levelVisited:
                                q.append(neiWord)
                                levelVisited.add(neiWord)
                            parents[neiWord].append(word)
                        elif neiWord in levelVisited and word not in parents[neiWord]:
                            parents[neiWord].append(word)
            visited.update(levelVisited)

        if not found:
            return []

        res, path = [], [endWord]

        def backtrack(word):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                backtrack(p)
                path.pop()

        backtrack(endWord)
        return res
