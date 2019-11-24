# https://leetcode.com/problems/add-binary/submissions/

# Brute
# Covert to int, compute sum and convert sum back
# return '{0:b}'.format(int(a, 2) + int(b, 2))
# O(m+n)
# WHY THIS DOESN'T WORK?
# 1. Won't fit into integer for JAVA Integer(33 1-bit) or Long(65 1-bit) or BigInteger(5 * 10^8+1)
# 2. Low performance on large input

# Bit by Bit computation
# O(max(M,N))
# O(max(M,N))
class Solution(object):
    def addBinary(self, a, b):
        n = max(len(a), len(b))
        a = '0'*(n-len(a)) + a
        b = '0'*(n-len(b)) + b
        carry = 0
        res = []

        for i in range(n-1, -1, -1):
            l = int(a[i])
            r = int(b[i])
            if carry == 1:
                if l == 0 and r == 0:
                    res.append('1')
                    carry = 0
                elif l == 1 and r == 1:
                    res.append('1')
                else:
                    res.append('0')
            else:
                if l == 1 and r == 1:
                    res.append('0')
                    carry = 1
                elif l == 0 and r == 0:
                    res.append('0')
                else:
                    res.append('1')
        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)

# More Concise Bit by Bit
    def addBinary(self, a, b):
        i, j, carry, res = len(a) - 1, len(b) - 1, 0, ""
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res = str(carry % 2) + res
            carry //= 2
        return res

# BIT Manipulation (NO ADDITION OPERATION)
# XOR :00 or 11-> 0, 01 or 10 -> 1
# O(N+M)
# O(max(M,N)) keeps the answer
    class Solution(object):
        def addBinary(self, a, b):
            a = int(a, 2)
            b = int(b, 2)
            carry = 1
            res = 0
            while carry:
                res = a ^ b
                carry = (a & b) << 1
                a = res
                b = carry
            return str(bin(res)[2:])

# Recursive

    def addBinary(self, a, b):
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'