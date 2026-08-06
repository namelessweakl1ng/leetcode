class Solution(object):
    def maximumSubarraySum(self, nums, k):
        curr_sum = 0
        prev_idx = {}
        l=0
        res =0

        for r in range(len(nums)):
            curr_sum +=nums[r]
            i = prev_idx.get(nums[r],-1) # copy the idx of the number that we are seeing on to the i
            prev_idx[nums[r]] =r # this will update the recently seen number index
            while l<=i or r-l+1>k:
                curr_sum-=nums[l]
                l+=1
            if r-l+1 ==k:
                res = max(res,curr_sum)
        return res