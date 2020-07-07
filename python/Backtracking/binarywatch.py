hours = [8,4,2,1,3]
minutes = [32,16,8,4]
class Solution:
    def __init__(self):
        self.hour = list()
        self.hour1 = list()
        self.minute  = list()
        self.minute1 = list()
    def hourCombi(self,hours,curr,count):
        if curr > 12:
            return
        if curr <=12 and str(curr) not in self.hour1 and curr != 0:
            self.hour1.append(str(curr))
            self.hour.append((str(curr),count))
        for hour in hours:
            if curr < 12:
                self.hourCombi(hours,curr+hour,count+1)
            else:
                return
    def minuteCombi(self,minutes,curr,count):
        if curr > 60:
            return
        if curr <=60 and str(curr) not in self.minute1 and curr != 0:
            self.minute1.append(str(curr))
            self.minute.append((str(curr),count))
        for minute in minutes:
            if curr < 60:
                self.minuteCombi(minutes,curr+minute,count+1)
            else:
                return
    def correctCombinations(self,nums):
        arrH = list()
        arrM = list()
        for i in range(len(self.hour)):
            if (self.hour[i][1]<=nums):
                arrH.append(self.hour[i])
        for j in range(len(self.minute)):
            if (self.minute[j][1]<=nums):
                arrM.append(self.minute[j])
        flag = 0
        flag1 = 0
        for i in range(len(arrH)):
            if (arrH[i][1]==nums):
                flag = 1
            else:
                flag = 0
                break
        for i in range(len(arrM)):
            if (arrM[i][1]==nums):
                flag1 = 1
            else:
                flag1 = 0
                break
        if flag == 1 and flag1 == 1:
            for i in arrH : 
                arrM.append(i)
            return arrM
        else:
            arr = list()
            for tup in arrH:
                if (tup[1]==nums):
                    arr.append(tup)
            for tup2 in arrM:
                if (tup2[1]==nums):
                    arr.append(tup2)
            for hourTuple in arrH:
                for minTuple in arrM:
                    if (hourTuple[1]+minTuple[1]==nums):
                        arr.append((hourTuple[0]+":"+minTuple[0],hourTuple[1]+minTuple[1]))
            return arr

s = Solution()
s.hourCombi(hours,0,0)
s.minuteCombi(minutes,0,0)
arr = s.correctCombinations(2)
print(arr)