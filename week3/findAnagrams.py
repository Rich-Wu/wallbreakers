from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = list(p)
        p.sort()
        matches = []
        for index in range(len(s) - len(p) + 1):
            substring = sorted(s[index: index + len(p)])
            if p == substring:
                matches.append(index)
        return matches