from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return next((Counter(t) - Counter(s)).elements())
