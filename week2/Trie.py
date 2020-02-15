class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False
        self.letters = [None for _ in range(26)]
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        index = ord(word[0]) - 65
        self.letters[index] = Trie()
        node = self.letters[index]
        for letter in word[1:]:
            index = ord(letter) - 65
            node.letters[index] = Trie()
            node = node.letters[index]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        index = ord(letter) - 65
        node = self.letters[index]
        for letter in word[1:]:
            index = ord(letter) - 65
            node = self.letters[index]
            if not node:
                return False
        if node.isEnd:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
