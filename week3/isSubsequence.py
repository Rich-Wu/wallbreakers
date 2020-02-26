class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        ps = 0
        for letter in t:
            if letter == s[ps]:
                ps += 1
            if ps == len(s): return True
        return ps == len(s)