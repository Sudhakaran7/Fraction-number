class Solution(object):
    def simplifiedFractions(self, n):
        def gcd(m, n):
            if not n:
                return m
            else:
                return gcd(n, m % n)
        res = []
        for i in range(1,n+1):
            for j in range(1,i):
                if gcd(i,j) == 1:
                    res.append(str(j) + '/' + str(i))
        return res
val=Solution()
n=int(input())
print(*val.simplifiedFractions(n))
