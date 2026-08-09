class Solution(object):
    def missingNumber(self, nums):
        res = len(nums)

        for i in range(len(nums)): # this is mathematical there is no way you can figure this out understand it with dry run
            res += (i-nums[i])
        return res