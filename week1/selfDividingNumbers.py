from typing import List

class Solution:    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for num in range(left, right + 1):
            if check_digits(self, num):
                nums.append(num)
        return nums
    
def check_digits(self, number: int) -> bool:
    checker = str(number)
    for digit in checker:
        if int(digit) == 0:
            return False
        if number % int(digit) != 0:
            return False
    return True