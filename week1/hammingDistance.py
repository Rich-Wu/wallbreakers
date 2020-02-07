class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        xor = ("{0:b}").format(x ^ y)
        for char in xor:
            if char == "1":
                count += 1
        return count