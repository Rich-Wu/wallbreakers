from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter()
        ans = [None, None]
        min_num = float('inf')
        max_num = float('-inf')
        for num in nums:
            counts[num] += 1
            if num > max_num: max_num = num
            if num < min_num: min_num = num
            if counts[num] > 1:
                ans[0] = num
        for num in range(1, max_num + 2):
            if num not in counts:
                ans[1] = num
                return ans
