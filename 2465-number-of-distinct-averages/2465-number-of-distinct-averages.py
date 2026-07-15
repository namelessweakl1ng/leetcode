class Solution(object):
    def distinctAverages(self, nums):
        res =[]
        while nums:
            max_num = max(nums)
            nums.remove(max_num)

            min_num = min(nums)
            nums.remove(min_num)
            
            avg = float(max_num+min_num)/2
            res.append(avg)
        return len(set(res))
