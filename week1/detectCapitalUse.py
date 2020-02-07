class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        first = word[0].isupper()
        for letter in word:
            if letter.isupper():
                count += 1
        return True if count == 0 or count == len(word) or (first and count == 1) else False