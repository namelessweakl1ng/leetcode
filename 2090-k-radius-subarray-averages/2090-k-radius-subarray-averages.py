class Solution(object):
    def getAverages(self, nums, k):
        n=len(nums)
        ans=[-1]*n
        if k == 0:
            return nums
        window = 2 * k +1
        if window > n:
            return ans
        curr_sum = sum(nums[:window])
        ans[k]= curr_sum//window
        for i in range(window,n):
            curr_sum += nums[i]
            curr_sum -= nums[i-window]
            ans[i-k] = curr_sum//window
        return ans