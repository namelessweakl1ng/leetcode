class Solution:
    def missingNumber(self, nums):
        missing = len(nums)

        for i in range(len(nums)):
            missing ^= i ^ nums[i] # this will XOR everything out leaving the number 2 in example one 

        return missing