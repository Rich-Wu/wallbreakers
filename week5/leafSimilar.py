# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return False
        res1 = [root1]
        leaf1 = []
        res2 = [root2]
        leaf2 = []
        while res1:
            node = res1.pop()
            if not node.left and not node.right:
                leaf1.append(node.val)
            if node.left:
                res1.append(node.left)
            if node.right:
                res1.append(node.right)
        while res2:
            node = res2.pop()
            if not node.left and not node.right:
                leaf2.append(node.val)
            if node.left:
                res2.append(node.left)
            if node.right:
                res2.append(node.right)
        return leaf1 == leaf2