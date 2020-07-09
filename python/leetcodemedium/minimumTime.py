points = [[1,1],[3,4],[-1,0]]
class Solution:
    def __init__(self):
        self.arr = list()
    def visitPoints(self, start, end, i, j,arr1):
        if end == (i,j):
            arr1.append((i,j))
            self.arr.append(arr1)
            return self.arr
        if (i >= min(start[0],end[0]) and i < max(end[1],start[1])) and j <= max(end[1],start[1]) and (i,j) not in arr1:
            arr1.append((i,j))
        else:
            return 
        #self.visitPoints(start,end,i+1,j)
        # self.visitPoints(start,end,i-1,j)
        # self.visitPoints(start,end,i,j+1)
        # self.visitPoints(start,end,i,j-1)
        self.visitPoints(start,end,i+1,j+1,arr1)
        self.visitPoints(start,end,i,j+1,arr1)
        # self.visitPoints(start,end,i-1,j+1)
        # self.visitPoints(start,end,i-1,j-1)
        # self.visitPoints(start,end,i+1,j-1)
s = Solution()
arr1 = list()
s.visitPoints((1,1),(3,4),1,1,arr1)
print(s.arr)