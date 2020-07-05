class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        i=0
        l=sorted(A)
        print("",l)

        while i<len(A):
            l[i]=l[i]*l[i]
            i=i+1
        k = sorted(l)
        return k

sol  = Solution()
A = [-4,-1,0,3,10]
l = sol.sortedSquares(A)
print("",l)