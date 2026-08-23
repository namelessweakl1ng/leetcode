class Solution(object):
    def check(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i]> nums[(i + 1) % len(nums)]: # if you want to ever rotate just get the reminder of i+1 to the len(nums)
                count+=1
        return count<=1