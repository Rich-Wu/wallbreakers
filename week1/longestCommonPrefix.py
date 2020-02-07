from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        prefix = strs[0]
        for word in strs[1:]:
            prefix = findPrefix(self, prefix, word)
        return prefix
    
def findPrefix(self, prefix: str, word: str) -> str:
    working_prefix = ""
    for letter_index in range(0, len(prefix)):
        if letter_index > len(word) - 1:
            return working_prefix
        if word[letter_index] != prefix[letter_index]:
            return word[0:letter_index]
        working_prefix += word[letter_index]
    return working_prefix