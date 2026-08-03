class Solution(object):
    def maxProduct(self, nums):
        curr_max = curr_min = ans = nums[0]

        for num in nums[1:]:
            tmp = curr_max
            # keep considering max and min until you get the max vaule keep comparing the value to get the ans
            # [MIN, MAX]
            curr_max = max(num, curr_max*num , curr_min*num)
            curr_min = min(num,tmp*num,curr_min*num)
            ans = max(ans,curr_max)
        return ans