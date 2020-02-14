class SetNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [None for _ in range(1024)]
        

    def add(self, key: int) -> None:
        bucket = key % len(self.buckets)
        if not self.buckets[bucket]:
            self.buckets[bucket] = SetNode(key)
        node = self.buckets[bucket]
        nextNode = node.next
        while node:
            if node.key == key:
                return
            if not node.next:
                node.next = SetNode(key)
                return
            node = node.next
            nextNode = nextNode.next
        return

    def remove(self, key: int) -> None:
        bucket = key % len(self.buckets)
        head = self.buckets[bucket]
        if not head:
            return
        node = head
        nextNode = head.next
        if node.key == key:
            self.buckets[bucket] = nextNode
        while nextNode:
            if nextNode.key == key:
                node.next = nextNode.next
                return
            nextNode = nextNode.next
            node = node.next
        return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = key % len(self.buckets)
        node = self.buckets[bucket]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
