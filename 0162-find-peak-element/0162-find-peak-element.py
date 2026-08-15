class Solution(object):
    def findPeakElement(self, nums):
        l , r = 0, len(nums)-1

        while l<=r:
            m = l + ((r-l)//2)
            if m>0 and nums[m] <nums[m-1]:
                r = m -1
            elif m+1< len(nums) and nums[m] < nums[m+1]:
                l = m +1
            else:
                return m
            