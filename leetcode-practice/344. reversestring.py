class Solution(object):
    def reversestring(self, s):
        i = 0
        n = len(s)
        for i in range (n // 2):
                s[i], s[n-i-1] = s[n-i-1], s[i]
        return ''.join(s)
sol = Solution()
s = ['h', 'e', 'l', 'l', 'o']
print(sol.reversestring(s))




