from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        sorted = ''
        counter = Counter(s)
        for letter in counter.most_common(len(counter)):
            sorted += letter[0] * letter[1]
        return sorted
