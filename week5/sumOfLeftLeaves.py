from typing import Type

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: Type[TreeNode]) -> int:
        if not root:
            return 0
        toVisit = []
        left_leaves = 0
        node = root
        while node:
            if node.left:
                toVisit.append(node.left)
                if not node.left.left and not node.left.right:
                    left_leaves += node.left.val
            if node.right:
                toVisit.append(node.right)
            if len(toVisit) > 0:
                node = toVisit.pop()
            else:
                return left_leaves