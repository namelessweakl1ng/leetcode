class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        product = 1
        answer = 0
        left = 0
        for right in range(len(nums)):
            product *= nums[right]

            while product >=k:
                product =product // nums[left]
                left +=1
            answer += right - left +1
        return answer
        