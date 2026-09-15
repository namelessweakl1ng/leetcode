class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        res = 1
        longest = 1
        num_set = sorted(set(nums))
        for i in range(1,len(num_set)):
            if num_set[i] == num_set[i - 1] + 1:
                longest+=1
            else:
                longest =1
            res = max(res,longest)
        return res