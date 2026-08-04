class Solution(object):
    def waysToSplitArray(self, nums):
        right = sum(nums) # get all the sum
        left = res = 0
            # for loop to move left and add the element while incrementing the result variable if the condition is satisfied
        for i in range(len(nums)-1):
            left +=nums[i]
            right -=nums[i]

            if left>=right: res+=1
        return res