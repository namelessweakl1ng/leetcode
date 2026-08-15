class Solution(object):
    def longestSubsequence(self, nums):
        xor_res = 0
        
        for num in nums:
            xor_res ^=num
        
        if xor_res!=0:
            return len(nums)
        
        for num in nums:
            if num!=0:
                return len(nums)-1 # logic is that if the reult is 0 then if you remove just one non zero element the total result become non- zero
        return 0
