from typing import Type

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: Type[ListNode]) -> Type[ListNode]:
        newNext = None
        node = head
        while node:
            nextNode = node.next
            node.next = newNext
            newNext = node
            if not nextNode:
                return node
            node = nextNode