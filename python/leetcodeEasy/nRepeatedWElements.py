import collections
class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        c = collections.Counter(A)
        for x in c:
            if c[x]> 1:
                return x


sol  = Solution()
nums = [1,2,3,3]
l = sol.repeatedNTimes(nums)
print("",l)