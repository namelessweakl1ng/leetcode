class Solution(object):
    def maximumSubarraySum(self, nums, k):
        res = 0
        count = defaultdict(int)
        curr_sum = 0
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            count[nums[r]]+=1

            if r-l+1>k:
                count[nums[l]]-=1
                curr_sum-=nums[l]
                if count[nums[l]]==0:
                    count.pop(nums[l])
                l+=1

            if r- l+1 == k == len(count):
                res= max(res,curr_sum)
        return res