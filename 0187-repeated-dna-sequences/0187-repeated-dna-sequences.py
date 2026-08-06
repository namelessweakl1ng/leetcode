class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen, res = set(),set()
        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                res.add(s[i:i+10])
            else:
                seen.add(s[i:i+10])
        return list(res)