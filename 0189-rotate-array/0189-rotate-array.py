class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n # for rotation
        nums[:] = nums[n-k:]+ nums[:n-k] # splitting and then putting it back