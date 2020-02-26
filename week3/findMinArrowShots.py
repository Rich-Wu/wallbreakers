from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        balloons = []
        points.sort(key = lambda x: x[1])
        current = points[0]
        for balloon in points[1:]:
            if balloon[0] > current[1]:
                balloons.append(current)
                current = balloon
                continue
            current[0] = max(current[0], balloon[0])
            current[1] = min(current[1], balloon[1])
        balloons.append(current)
        return len(balloons)