class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        product = 1
        answer = 0
        left = 0
        for right in range(len(nums)):
            #multiples the numbers in nums
            product *= nums[right]
            #if the value surpases the k value
            while product >=k:
                product =product // nums[left]
                left +=1
            # when it fits then add it to the answr as count
            answer += right - left +1
        return answer
        