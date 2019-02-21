class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        odd = list()
        even  = list()
        result = list()
        for x in range(len(A)):
            if A[x]%2!=0:
                odd.append(A[x])
            else:
                even.append(A[x])
        result = even + odd
        return result
sol  = Solution()
nums = [0,1,1,2]
l = sol.sortArrayByParity(nums)
print("",l)