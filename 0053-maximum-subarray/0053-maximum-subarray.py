class Solution(object):
    def maxSubArray(self, nums):
        max_sub = nums[0]
        currsum = 0
        for n in nums:
            if currsum<0:
                currsum = 0
            currsum+=n
            max_sub = max(max_sub,currsum)
        return max_sub