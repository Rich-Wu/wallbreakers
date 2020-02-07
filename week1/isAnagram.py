class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charBank = {}
        for char in s:
            if char in charBank:
                charBank[char] += 1
            else:
                charBank[char] = 1
        for char in t:
            if char in charBank:
                charBank[char] -= 1
                if charBank[char] < 0:
                    return False
            else:
                return False
        for char in charBank:
            if charBank[char] != 0:
                return False
        return True