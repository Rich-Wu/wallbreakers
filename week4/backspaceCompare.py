class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        st1 = []
        st2 = []
        for char in S:
            if char == "#":
                if st1:
                    st1.pop()
            else:
                st1.append(char)
        for char in T:
            if char == "#":
                if st2:
                    st2.pop()
            else:
                st2.append(char)
        return st1 == st2