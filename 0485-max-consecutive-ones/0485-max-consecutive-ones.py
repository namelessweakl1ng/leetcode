class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l =0 
        count = 0
        res= 0

        for r in range(len(nums)):
            if nums[r]:
                count+=1
            else:
                l = r
                count =0
            res = max(count,res)
        return res 
