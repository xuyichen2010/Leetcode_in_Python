# O(n^2) ??? because w[1:] takes O since str is immutable in Python
# O(n)
class Solution(object):
    def toGoatLatin(self, S):
        out = []
        for i, w in enumerate(S.split(' ')):
            if w[0] not in list('aeiouAEIOU'):
                w = w[1:] + w[0]
            out.append(w + 'ma' + 'a'*(i+1))
        return ' '.join(out)