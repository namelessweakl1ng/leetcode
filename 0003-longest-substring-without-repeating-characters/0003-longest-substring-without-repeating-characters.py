class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = {} # make a hashMap
        left = 0
        max_str = 0

        for right in range(len(s)):
            if s[right] in res: # if the value is in the res already 
                left = max(left,res[s[right]]+1) # max() because of the abba case 
            res[s[right]]=right # assigning the index 
            max_str = max(max_str,right-left +1) # max of the substring
        return max_str