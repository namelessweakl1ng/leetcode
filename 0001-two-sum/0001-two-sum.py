class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for i,v in enumerate(nums):
            diff = target-v
            if diff in hashMap:
                return [i,hashMap[diff]]
            hashMap[v]=i