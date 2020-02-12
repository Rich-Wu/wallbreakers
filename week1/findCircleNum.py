from typing import List

# Naive Union Find Object with just parent reference
class DisjointSetNode:
    def __init__(self):
        self.parent = self
        
    def find(self) -> 'DisjointSetNode':
        while (self.parent != self):
            self = self.parent
        return self

    def union(self, node2: 'DisjointSetNode') -> None:
        self = self.find()
        node2_root = node2.find()
        if self != node2_root:
            node2_root.parent = self
        else:
            return

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # Initialize an array; each node represents a person's friend circle, of whom only they are members of on initialization
        circles = [DisjointSetNode() for x, _ in enumerate(M)]
        for row_i, row in enumerate(M):
            for col_i, col in enumerate(row):
                # If two people are friends, one person's friend circle will point to the other's
                if col == 1:
                    circles[col_i].union(circles[row_i])
        # Set to count the number of unique root friends, who are representative of a friend circle
        ans = {*[friend.find() for friend in circles]}
        # Number of unique friends in the set is the number of unique friend circles
        return len(ans)