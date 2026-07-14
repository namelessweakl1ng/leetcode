class Solution(object):
    def isPowerOfFour(self, n):
        if n<0:
            return False
        for i in range(100):
            if n==4**i:
                return True
        return False
        