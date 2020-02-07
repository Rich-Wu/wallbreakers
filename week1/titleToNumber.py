class Solution:
    def titleToNumber(self, s: str) -> int:
        accumulator = 0
        current = 0
        for letter in reversed(s):
            accumulator += (ord(letter) - 64) * (26**current)
            current += 1
        return accumulator