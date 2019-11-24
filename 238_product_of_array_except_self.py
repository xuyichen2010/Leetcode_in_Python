# https://leetcode.com/problems/product-of-array-except-self/

#  L stores product of elements to the left
# R stores product of elemetns to the right
# O(n)
# O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        if not nums or len(nums) == 1:
            return 0
        l = [1]*len(nums)
        r = [1]*len(nums)
        for i in range(1, len(nums)):
            l[i] = l[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i+1]*nums[i+1]
        res = []
        for i in range(len(nums)):
            res.append(l[i]*r[i])
        return res


# Use result array to store l
# O(n)
# O(1) space
def productExceptSelf(self, nums):
    if not nums or len(nums) == 1:
        return 0
    res = [1] * len(nums)
    r = 1
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * r
        r *= nums[i]
    return res

# Cases considering zeros using division method
class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
            return []
        product = 1
        one_zero = False
        product2 = 1
        for item in nums:
            if item == 0 and one_zero:
                break
            elif item == 0:
                one_zero = True
                product *= item
            else:
                product *= item
                product2 *= item
        else:
            res = []
            for item in nums:
                if item == 0:
                    res.append(product2)
                else:
                    res.append(product//item)
            return res
        return [0]*len(nums)

# One for loop

def productExceptSelf(self, nums):
    res = [1]*len(nums)
    lprod = 1
    rprod = 1
    for i in range(len(nums)):
        res[i] *= lprod
        lprod *= nums[i]
        res[~i] *= rprod
        rprod *= nums[~i]
    return res