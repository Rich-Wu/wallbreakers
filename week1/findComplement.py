class Solution:
    def findComplement(self, num: int) -> int:
        binary = "{0:b}".format(num)
        complement = ""
        for num in binary:
            complement = complement + "1" if num == "0" else complement + "0"
        return int(complement, 2)