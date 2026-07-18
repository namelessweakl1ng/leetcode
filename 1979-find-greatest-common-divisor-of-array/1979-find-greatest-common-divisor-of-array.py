class Solution(object):
    def findGCD(self, nums):
        def GCD(low, high):
            if high== 0:
                return low
            return GCD(high,low % high) 
        return GCD(min(nums),max(nums))
        