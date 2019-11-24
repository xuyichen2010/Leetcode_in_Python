# https://leetcode.com/problems/add-strings/

# O(max(n,m))
# O(n)
class Solution(object):
    def addStrings(self, num1, num2):
        p1 = len(num1)-1
        p2 = len(num2)-1
        res = []
        carry = 0
        dict = {'0':0,'1':1,'2':2,'3':3,'5':5,'6':6,'7':7,'8':8,'9':9,'4':4}
        while p1 >= 0 and p2 >= 0:
            res.append(str((dict[num1[p1]] + dict[num2[p2]] + carry)%10))
            carry = (dict[num1[p1]] + dict[num2[p2]] + carry)//10
            p1 -= 1
            p2 -= 1
        while p1 >= 0:
            res.append(str((dict[num1[p1]] + carry)%10))
            carry = (dict[num1[p1]] + carry)//10
            p1 -=1
        while p2 >= 0:
            res.append(str((dict[num2[p2]] + carry)%10))
            carry = (dict[num2[p2]] + carry)//10
            p2 -=1
        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)