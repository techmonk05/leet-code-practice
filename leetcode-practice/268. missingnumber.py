class Solution(object):
    def missingnumber(self, nums):
        i = 0
        n = len(nums)
        while (i < n):
            cin = nums[i]
            if cin < n and nums[i] != nums[cin]:
                nums[i], nums[cin] = nums[cin], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        return n
s = Solution()
nums = [3,0,1]
y = s.missingnumber(nums)
print(y)

