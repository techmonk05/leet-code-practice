class Solution(object):
    def subtractproductandsum(self, n):
        i: int = 0
        s: int = 0
        p: int = 1
        while n > 0:
            i = n % 10
            n = int (n / 10)
            s = s + i
            p = p * i
        res = p - s
        return res
sol = Solution()
n = 512
y = sol.subtractproductandsum(n)
print(y)



