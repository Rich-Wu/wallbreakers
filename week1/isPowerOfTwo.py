class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        count = 0
        str_n = "{0:b}".format(n)
        for place in str_n:
            if place == "1":
                count += 1
            if count > 1:
                return False
        return True if bool(count) else False