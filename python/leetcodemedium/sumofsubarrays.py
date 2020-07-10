A = [3,8,1,3,2,1,8,9,0]
L = 3
M = 2
class Solution:
    def __init__(self):
        self.arr = list()
    def maxsum(self,A,L,a,count):
        if len(A) < L:
            n = len(A)%L
            for i in range(n):
                A.append(0)
        if count <= L and count <=len(a):
            if count < L:
                a.append(A[count])
                count = count + 1
            elif count == L:
                self.arr.append(a)
                return self.arr
            else:
                return
        if count>L:
            return
        self.maxsum(A,L,a,count)
s = Solution()
for i in range(len(A)):
    s.maxsum(A[i:],L,[],0)
a1 = s.arr.copy()
s.arr.clear()
for i in range(len(A)):
    s.maxsum(A[i:],M,[],0)
a2 = s.arr.copy()
a3 = list()
s = 0
print(a1)
print(a2)
maxsum = 0
for i in range(len(A)):
    for j in range(len(A)):
        check =  any(item in a1[i] for item in a2[j])
        if not check and i!=j:
            tempsum = sum(a1[i]) + sum(a2[j])
            if tempsum > maxsum:
                print(a1[i])
                print(a2[j])
                maxsum = tempsum
print(maxsum)
