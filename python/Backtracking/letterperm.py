class Solution:
    def __init__(self):
        self.arr = list()
    def letterCasePermutation(self, S,curr,length):
        if (length==len(curr) and curr not in self.arr):
            return self.arr.append(curr)
        if curr in self.arr:
            return
        for i in range(len(S)):
            if len(curr) <= length:
                if S[i] not in curr:
                    self.letterCasePermutation(S,curr+S[i],length)
            else:
                return
arr = "a1b2"
s = Solution()
s.letterCasePermutation(arr,"",4)
print(s.arr)