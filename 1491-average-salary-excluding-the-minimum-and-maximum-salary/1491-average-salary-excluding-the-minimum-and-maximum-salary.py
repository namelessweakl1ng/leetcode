class Solution(object):
    def average(self, salary):
        sum =0
        count=0
        for num in salary:
            sum +=num
            count+=1
        return float((sum - min(salary) - max(salary))) / (count - 2)