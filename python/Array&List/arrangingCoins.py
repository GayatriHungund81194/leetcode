class Solution:
    def arrangeCoins(self, n: 'int') -> 'int':
        
        rowCount=0
        StarCount=n-1
        if n==1 or n==2:
            rowCount=1
            return rowCount
        elif n==3 or n==4:
            rowCount=2
            return rowCount
        else:
            for x in range(n):
                if StarCount >= n-StarCount:
                    for y in range(n-StarCount):
                        print("*",end="")
                    StarCount=StarCount-1
                    rowCount = rowCount+1
                    print("\r")
            return rowCount
        

sol  = Solution()
nums = 8
sol.arrangeCoins(nums)
