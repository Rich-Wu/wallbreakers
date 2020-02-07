from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        digits[len(digits) - 1] += 1
        for digit_index in range(len(digits) - 1, -1, -1):
            if carry:
                digits[digit_index] += 1
                carry = False
            if digits[digit_index] > 9:
                carry = True
                digits[digit_index] %= 10
        if carry:
            digits.insert(0, 1)
        return digits