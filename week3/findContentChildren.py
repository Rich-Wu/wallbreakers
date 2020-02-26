from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        gP = len(g) - 1
        sP = len(s) - 1
        if len(g) == 0 or len(s) == 0:
            return 0
        while gP >= 0 and sP >= 0:
            cookie = s[sP]
            child = g[gP]
            # print("child at index {0}: {1} cookie at index {2}: {3}".format(gP, child, sP, cookie))
            if cookie >= child:
                count += 1
                sP -= 1
            gP -= 1
        return count