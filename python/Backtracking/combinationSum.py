class Solution:
    def __init__(self):
        self.arr = list()
    def combinationSum(self, candidates, target, elem,summation):
        if len(elem)>1:
            if elem[-1] < elem[-2]:
                return
        if summation == target:
            return self.arr.append(elem)
        for candidate in candidates:
            if summation+candidate <= target:
                self.combinationSum(candidates,target,elem+[candidate],summation+candidate)
            else:
                return
s = Solution()
candidates = [8,7,4,3]
candidates.sort()
arr = []
s.combinationSum(candidates,11,arr,0)
print(s.arr)
