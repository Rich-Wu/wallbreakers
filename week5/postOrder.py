from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = []
        out = []
        node = root
        while node:
            if node.children:
                stack += node.children
            out.append(node.val)
            if stack:
                node = stack.pop()
            else:
                return out[::-1]