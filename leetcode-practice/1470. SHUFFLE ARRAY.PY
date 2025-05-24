class Solution(object):
    def shuffle(self, nums, n):
        j = 0
        k = n
        res = [0] * (2 * n)
        i = 0
        for i in range (2 * n):
            if i % 2 == 0:
                res[i] = nums[j]
                j += 1
            else:
                res[i] = nums[k]
                k += 1
        return res
s = Solution()
nums = [2,5,1,3,4,7]
n = 3
y = s.shuffle(nums,n)
print(y)


