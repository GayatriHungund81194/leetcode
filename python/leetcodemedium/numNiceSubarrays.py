class Solution:
    def __init__(self):
        self.a1 = list()

    def findOdd(self,arr,k):
        oddcount = 0
        totalcount = 0
        for eachArr in arr:

            for i in range(len(eachArr)):   
                if eachArr[i]%2!=0:
                    oddcount = oddcount + 1
            if oddcount == k:
                totalcount = totalcount + 1
            oddcount = 0
            print(eachArr)
            print(totalcount)
        return totalcount

    def getSubarrays(self,a,arr,k,count):
        if k == count:
            self.a1.append(arr)
            return self.a1
        if count > k:
            return
        if count < k and len(a)!=0:
            arr.append(a[count])
        else:
            return
        self.getSubarrays(a,arr,k,count+1)
s = Solution()
a = [1,1,2,1,1]
k = 3
for j in range(k,len(a)+1):
    for i in range(len(a)):
        if (len(a[i:])>=j):
            s.getSubarrays(a[i:],[],j,0)
print(s.a1)
o = s.findOdd(s.a1,k)
print(o)