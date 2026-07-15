
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        def GCD(a, b):
            while b:
                a, b = b, a % b
            return a

        sumeven = sumodd = 0

        for i in range(1, n + 1):
            sumeven += 2 * i
            sumodd += 2 * i - 1

        return GCD(sumodd, sumeven)