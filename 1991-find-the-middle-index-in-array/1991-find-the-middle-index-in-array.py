class Solution(object):
    def findMiddleIndex(self, nums):
        total = sum(nums) # take total of the entire array so that you can subtract the reset and compare
        left_sum = 0 # take the left sum as the 0 
        for i in range(len(nums)): # iterate throug the array till you find the middle value
            if left_sum == total - left_sum - nums[i]: # if the left_sum is rqual to the total - itself -nums[i] it must give us the right sum
                return i
            left_sum += nums[i] # if it doesnt then move forward
        return -1 