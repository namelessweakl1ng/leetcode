class Solution(object):
    def findErrorNums(self, nums):
        res = [0,0] # [duplicate , missing]

        count = Counter(nums) # example this gives for input nums = [1,2,2,4] => {2:2 , 1:1 , 4:1}
        for i in range(1,len(nums)+1): # going from 1 to len cuz its given in the contraints
            if count[i]==0:
                res[1]= i
            if count[i]==2:
                res[0] = i
        return res
