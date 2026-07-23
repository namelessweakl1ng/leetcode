class Solution(object):
    def uniqueXorTriplets(self, nums):
        return len(nums) if len(nums)<3 else 1<<len(nums).bit_length()