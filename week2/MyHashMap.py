class HashMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 1024 buckets
        self.buckets = [None for _ in range(1024)]
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self.buckets[hash(key) % len(self.buckets)]
        newNode = HashMapNode(key, value)
        if not bucket:
            self.buckets[hash(key) % len(self.buckets)] = newNode
        else:
            node = bucket
            while node:
                if node.key == key:
                    node.value = value
                    return
                if node.next:
                    node = node.next
                else:
                    node.next = newNode
                    return
            return
            

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        node = self.buckets[hash(key) % len(self.buckets)]
        while node:
            if node.key == key:
                return node.value
            else:
                node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self.buckets[hash(key) % len(self.buckets)]
        if bucket:
            if bucket.key == key:
                self.buckets[hash(key) % len(self.buckets)] = bucket.next
                return
            else:
                node = bucket
                nextNode = bucket.next
                while nextNode:
                    if nextNode.key == key:
                        node.next = nextNode.next
                    nextNode = nextNode.next
                    node = node.next
                return
        return
            
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
