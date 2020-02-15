from collections import Counter
import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower().translate("".maketrans(string.punctuation," " * len(string.punctuation)))
        print(paragraph)
        counts = Counter([word for word in paragraph.split() if word not in banned])
        print(counts)
        return counts.most_common(1)[0][0]
