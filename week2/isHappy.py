class Solution:
    def isHappy(self, n: int) -> bool:
        # Remembers numbers that have been seen
        seen = set()
        while n != 1:
            num = n
            acc = 0
            # Finds the sum of all the squares of each digit in num
            while num != 0:
                acc = (acc + (num % 10) ** 2)
                num = num // 10
            # Checks if the sum has been seen before, which would denote an infinite loop
            if acc in seen:
                return False
            # Records the occurrence of this number, for future comparisons
            seen.add(acc)
            n = acc
        return True