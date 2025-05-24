class Solution(object):
    def mysqrt(self, x):
        s = 1
        e = x
        res = 0
        if x == 0 or x == 1: return x
        if x < 0: return -1
        while s <= e:
            m = (s + e) //2
            if (m * m) > x:
                e = m - 1
            elif (m * m) < x:
                s = m + 1
                res = m
            elif (m * m) == x:
                return m
        return res
s = Solution()
yy = 400
y = s.mysqrt(yy)
print(y)

