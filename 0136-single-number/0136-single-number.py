class Solution(object):
    def singleNumber(self, nums):
        Hashmap = collections.defaultdict(int)
        for num in nums:
            Hashmap[num]+=1
        for num in nums:
            if Hashmap[num]==1:
                return num
        return -1
        