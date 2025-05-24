class Solution(object):
    def plusone(self, digits):
        digits = digits[::-1]
        c,i = 1,0
        while c :
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    c = 0
            else:
                digits.append(1)
                c= 0
            i +=1
        return digits[::-1]
sol = Solution()
digits = [9]
y = sol.plusone(digits)
print(y)

