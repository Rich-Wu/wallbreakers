from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, letter in enumerate(s):
            if counts[letter] == 1:
                return i
        return -1
