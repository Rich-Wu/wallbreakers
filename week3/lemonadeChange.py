from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for sale in bills:
            if sale == 5:
                fives += 1
            elif sale == 10:
                fives -= 1
                tens += 1
            elif sale == 20:
                if tens >= 1:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0 or tens < 0:
                return False
        return True