from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = dict(zip('abcdefghijklmnopqrstuvwxyz', [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
        wordSet = set()
        for word in words:
            convert = ""
            for letter in word:
                convert += code[letter]
            wordSet.add(convert)
        return len(wordSet)