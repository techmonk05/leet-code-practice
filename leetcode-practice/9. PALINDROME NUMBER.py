class Solution(object):
    def ispalindrome(self, x):
        rev = 0
        temp = x
        if x < 0:
            return False
        while x > 0:
            rem = x % 10
            x = x // 10
            rev = rev * 10 + rem
        if temp == rev:
            return True
        else:
            return False
s = Solution()
x = 121
y = s.ispalindrome(x)
print(y)






