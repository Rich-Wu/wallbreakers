class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            if s_dict.get(s[i], -1) != t_dict.get(t[i], -1):
                return False
            s_dict[s[i]] = t_dict[t[i]] = i
        return True