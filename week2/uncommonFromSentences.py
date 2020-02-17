from typing import List

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        seen = dict()
        for word in A.split(" "):
            seen[word] = 1 if word not in seen else seen[word] + 1
        for word in B.split(" "):
            seen[word] = 1 if word not in seen else seen[word] + 1
        return [word for word, count in seen.items() if count == 1]