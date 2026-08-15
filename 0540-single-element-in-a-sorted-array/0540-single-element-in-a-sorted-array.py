class Solution(object):
    def singleNonDuplicate(self, nums):
        # my solution
        count = collections.defaultdict(int)

        for num in nums:
            count[num]+=1
        for num in nums:
            if count[num] ==1:
                return num
        