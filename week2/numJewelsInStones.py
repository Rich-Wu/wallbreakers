class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = {}
        for jewel in J:
            count[jewel] = 0
        for rock in S:
            if rock in count:
                count[rock] += 1
        return sum(count.values())