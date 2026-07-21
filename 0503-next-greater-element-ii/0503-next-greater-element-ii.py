class Solution(object):
    def nextGreaterElements(self, nums):
        ans = []
        for i in range(len(nums)):
            greater =-1
            for k in range(1,len(nums)):
                j= (i+k)%len(nums)
                if nums[i]<nums[j]:
                    greater= nums[j]
                    break
            ans.append(greater)
        return ans
