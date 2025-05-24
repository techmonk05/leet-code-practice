class Solution(object):
    def majorityelement(self, nums):
        c = 0
        i,j = 0,0
        n = len(nums)
        nums.sort()
        while i < n :
            c = 1
            j = i + 1
            while j < n:
                if nums[j-1] == nums[j]:
                    c += 1
                    j += 1
                else: break
            i = j
            if c > n // 2:
                return nums[i-1]
        return -1



sol = Solution()
nums = [2,2,1,1,1,2,2]
y = sol.majorityelement(nums)
print(y)







