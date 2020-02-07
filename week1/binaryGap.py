class Solution:
    def binaryGap(self, N: int) -> int:
        max_dist = 0
        current_dist = 0
        started = False
        N = "{0:b}".format(N)
        for digit in N[::-1]:
            if started:
                current_dist += 1
                if digit == "1":
                    max_dist = max(max_dist, current_dist)
                    current_dist = 0
            else:
                if digit == "1":
                    started = True
        return max_dist