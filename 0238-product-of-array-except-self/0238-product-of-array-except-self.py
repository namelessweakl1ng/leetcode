class Solution(object):
    def productExceptSelf(self, nums):
        # well this is very easy if we get to use the time complexity we can use 2 for loops to iterate over the array and then we can get ans
        res = [1] * (len(nums)) # assign all the values of the list as 1 
        prefix = 1
        for i in range(len(nums)):
            res[i]= prefix 
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1): # go from last each step with -1
            res[i]*= postfix
            postfix*= nums[i]
        return res