from collections import defaultdict
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMost(k):
            count = defaultdict(int)
            left = 0
            ans = 0
            for right in range(len(nums)):
                if count[nums[right]]==0:
                    k-=1
                count[nums[right]]+=1
                while k<0:
                    count[nums[left]]-=1
                    if count[nums[left]]==0:
                        k+=1
                    left+=1
                ans += right -left+1
            return ans
        return atMost(k) - atMost(k-1)
