class Solution(object):
    def longestcommonprefix(self, strs):
        if not strs:
            return ""
        if len(strs[0]) == 0:
            return ""
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: #checking for edge cases where it goes out of bound and when its no longer equal to the prefix
                    return res
            res += strs[0][i]
        return res
sol = Solution()
strs = ["dog","dogracecar","dogcar"]
y = sol.longestcommonprefix(strs)
print(y)


