from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        p_length = len(p)
        ans = []
        s_count = Counter()
        for i in range(len(s) - len(p) + 1):
            if i == 0:
                s_count = Counter(s[0:p_length])
            else:
                s_count[s[i + p_length - 1]] += 1
                s_count[s[i - 1]] -= 1
                if s_count[s[i - 1]] == 0:
                    del s_count[s[i - 1]]
            if s_count == p_count:
                ans.append(i)
        return ans