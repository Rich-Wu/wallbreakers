class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = ""
        for _ in reversed(s):
            reverse += _
        reverse = reverse.split(" ")
        return " ".join(reverse[::-1])