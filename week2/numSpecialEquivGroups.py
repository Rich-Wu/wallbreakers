from typing import List

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def create_two_set(word):
            out = [0] * 52
            for i, letter in enumerate(word):
                code = ord(letter) - ord('a')
                if i % 2 == 1:
                    code += 26
                out[code] += 1
            return tuple(out)        
        word_sets = set([create_two_set(word) for word in A])
        return len(word_sets)  