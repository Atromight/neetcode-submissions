class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        is_neg = False
        if n < 0:
            is_neg = True

        if is_neg:
            n = -n

        for i in range(n // 2):
            res *= (x*x)

        if n % 2 != 0:
            res *= x
        
        if is_neg:
            return 1/res

        else:
            return res