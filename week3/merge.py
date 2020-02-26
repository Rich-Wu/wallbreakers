from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        if not len(intervals):
            return merged
        intervals.sort(key = lambda x: x[0])
        current = intervals[0]
        for interval in intervals[1:]:
            if interval[0] > current[1]:
                merged.append(current)
                current = interval
                continue
            current[0] = min(interval[0], current[0])
            current[1] = max(interval[1], current[1])
        merged.append(current)
        return merged