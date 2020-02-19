class TrieNode:
    def __init__(self):
        self.letters = [None] * 26
        self.isEnd = False
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = [None] * 26
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root[get_index(word[0])]
        if not node:
            self.root[get_index(word[0])] = TrieNode()
        node = self.root[get_index(word[0])]
        for letter in word[1:]:
            pointer = node.letters[get_index(letter)]
            if not pointer:
                node.letters[get_index(letter)] = TrieNode()
            node = node.letters[get_index(letter)]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root[get_index(word[0])]
        if not node:
            return False
        for letter in word[1:]:
            node = node.letters[get_index(letter)]
            if not node:
                return False
        return node and node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root[get_index(prefix[0])]
        if not node:
            return False
        for letter in prefix[1:]:
            node = node.letters[get_index(letter)]
            if not node:
                return False
        return bool(node)
        
def get_index(letter: str) -> int:
    return ord(letter) - ord('a')

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)