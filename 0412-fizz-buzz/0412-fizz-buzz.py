class Solution(object):
    def fizzBuzz(self, n):
        res = []
        def is_buzz(n):
            if n%3==0 and n%5==0:
                return "FizzBuzz"
            elif n%3==0:
                return "Fizz"
            elif n%5==0:
                return "Buzz"
            else:
                return str(n)
            return n
        for val in range(1,n+1):
            res.append(is_buzz(val))
        return res