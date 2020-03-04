from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pos = {c: i for i, c in enumerate(nums2)}
        ans = [-1 for _ in range(len(nums1))]
        for i, num1 in enumerate(nums1):
            for index in range(pos[num1] + 1, len(nums2)):
                if nums2[index] > num1:
                    ans[i] = nums2[index]
                    break
        return ans