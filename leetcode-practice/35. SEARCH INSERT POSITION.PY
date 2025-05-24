class Solution(object):
    def searchInsert(self, nums, target):
        n =  len(nums)
        i = 0
        while(i<n):
            if nums[i] >= target:
                return i
            i+=1
        return n
sol = Solution()
nums = [1,2,3,4,5,6,7,8,9,11]
target = 10
y = sol.searchInsert(nums,target)
print(y)
