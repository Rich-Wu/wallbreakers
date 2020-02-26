class Solution(object):
    def partitionLabels(self, S):
        # Initializes dict with last occurrences of each letter
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            # moves j if the last occurrence of c is further along in the string
            j = max(j, last[c])
            # if i has reached j, adds the length of substring to ans
            if i == j:
                ans.append(i - anchor + 1)
                # Increment anchor to current index + 1 once a subsection has been found
                anchor = i + 1
        return ans