class Solution(object):
    def singleNumber(self, nums):
        count = collections.defaultdict(int)
        res =[]

        for num in nums:
            count[num]+=1
        for num in nums:
            if count[num]==1:
                res.append(num)
        return res