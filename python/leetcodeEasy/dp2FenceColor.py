# def paintFence(i,n,k):
#     if i == n:
#         return k
#     if i > n:
#         return 0
#     return paintFence(i+1,n,k) + paintFence(i+2,n,k)
# pf = paintFence(0,3,2)
# print(pf)
class Solution:
    def callnumWays(self, i: int, n: int, k: int):
        if n == 0:
            return 0
        if k == 1:
            return 1
        if i == n:
            return k
        if i > n:
            return 0
        return self.callnumWays(i+1,n,k) + self.callnumWays(i+2,n,k)
    
    def numWays(self, n: int, k: int) -> int:
        if n > k:
            nWays = self.callnumWays(0,n,k)
        return nWays
s = Solution()
col = s.numWays(3,1)
print(col)

