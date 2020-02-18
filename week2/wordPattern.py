class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # Init 2 dict
        pattern_dict, word_dict = {}, {}
        str = str.split(" ")
        if len(pattern) != len(str):
            return False
        for i in range(len(pattern)):
            # Checks if a letter/word already exists in one dict but not the other
            if pattern_dict.get(pattern[i], -1) != word_dict.get(str[i], -1):
                # If so, returns False
                return False
            # Sets one a letter to the index of a word in str and sets word to the index of a letter
            pattern_dict[pattern[i]] = word_dict[str[i]] = i
        return True