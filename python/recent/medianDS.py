from heapq import heappush, heappop, heappushpop
class MedianFinder:

    def __init__(self):
        self.upperHeap = [float('inf')]
        self.lowerHeap = [float('inf')]
        

    def addNum(self, num: int) -> None:
        upperMin = + self.upperHeap[0]
        lowerMax = - self.lowerHeap[0]
        print(upperMin)
        print(lowerMax)

        if num > upperMin or (lowerMax<=num<=upperMin and len(self.upperHeap)==len(self.lowerHeap)):
            heappush(self.upperHeap, num)
        else:
            heappush(self.lowerHeap, -num)

        if len(self.upperHeap)-len(self.lowerHeap) > 1:
            heappush( self.lowerHeap, -heappop( self.upperHeap ) )
        elif len(self.lowerHeap) > len(self.upperHeap):
            heappush( self.upperHeap, -heappop( self.lowerHeap ) )

    # def findMedian(self) -> float:
        
mf = MedianFinder()
mf.addNum(1)
mf.addNum(4)
mf.addNum(2)
mf.addNum(3)
mf.addNum(6)
