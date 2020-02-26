from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minSoFar = prices[0]
        visited = maxPossibleProfit([], prices, 0, minSoFar)
        return max(visited)
        
def maxPossibleProfit(self, prices, index, minSoFar):
    if index == len(prices):
        return self
    self.append(prices[index] - minSoFar if prices[index] - minSoFar > 0 else 0)
    if prices[index] < minSoFar:
        minSoFar = prices[index]
    return maxPossibleProfit(self, prices, index + 1, minSoFar)