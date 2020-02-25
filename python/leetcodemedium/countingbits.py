class Solution:
    def countBits(self, num: int):
        l = list()
        orig = num
        for i in range(orig+1):
            n = self.givebin(i)
            cnt = self.countOne(n)
            l.append(cnt)
        return l
            
    def givebin(self,num: int) -> str:
        st = ""
        if num == 1:
            return "1"
        elif num == 0:
            return "0"
        while num >= 1:
            rem = int(num % 2)
            print(rem)
            num = num / 2
            st = st + str(rem)
        print(st[::-1])
        return st[::-1]
    
    def countOne(self,one: str) -> int:
        count = 0
        for i in range(len(one)):
            if one[i] == "1":
                count = count + 1
        return count
s= Solution()
s.countBits(3)
