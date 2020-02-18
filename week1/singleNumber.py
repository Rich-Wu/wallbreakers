from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numMap = {}
        for num in nums:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
        for num in numMap:
            if numMap[num] == 1:
                return num