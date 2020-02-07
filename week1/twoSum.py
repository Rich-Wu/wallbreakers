from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for num_index in range(len(nums)):
            if (nums[num_index] in numMap):
                return [numMap[nums[num_index]], num_index]
            else:
                numMap[target - nums[num_index]] = num_index
        return []