from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        intersection = set()
        for num in nums1:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        for num in nums2:
            if num in seen:
                seen[num] -= 1
                intersection.add(num)
                if seen[num] <= 0:
                    del seen[num]
        return intersection
