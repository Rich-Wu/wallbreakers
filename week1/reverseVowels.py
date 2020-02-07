class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        lp = 0
        rp = len(s) - 1
        while (lp < rp):
            if s[lp] in vowels and s[rp] in vowels:
                temp = s[lp]
                s[lp] = s[rp]
                s[rp] = temp
                lp += 1
                rp -= 1
            elif s[lp] in vowels:
                rp -= 1
            elif s[rp] in vowels:
                lp += 1
            else:
                rp -= 1
                lp += 1
        return "".join(s)