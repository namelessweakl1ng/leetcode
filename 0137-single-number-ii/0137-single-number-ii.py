class Solution(object):
    def singleNumber(self, nums):
        count = collections.defaultdict(int)

        for num in nums:
            count[num]+=1
        for num in nums:
            if count[num]==1:
                return num
        return -1