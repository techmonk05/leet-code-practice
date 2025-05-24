class Solution(object):
    def kidswithcandies(self, candies, extraCandies):
        #max_candy = max(candies)
        max = candies[0]
        i = 0
        for i in range (len(candies)):
            if max <= candies[i]:
                max = candies[i]
        print(max)
        i = 0
        result = []
        while i < len(candies):
            if (candies[i] + extraCandies) >= max:
                result.append(True)
            else:
                result.append(False)
            i += 1
        return result
sol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
y = sol.kidswithcandies(candies, extraCandies)
print(y)