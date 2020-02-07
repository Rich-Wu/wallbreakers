class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        trimmed = ''
        for letter in s:
            lowercase = letter.lower()
            if lowercase in alphabet:
                trimmed += lowercase
        print(trimmed)
        return True if trimmed == trimmed[::-1] else False