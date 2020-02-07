from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lp = 0
        rp = len(s) - 1
        while (lp < rp):
            temp = s[lp]
            s[lp] = s[rp]
            s[rp] = temp
            lp += 1
            rp -= 1