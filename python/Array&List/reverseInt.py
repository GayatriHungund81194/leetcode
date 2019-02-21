class Solution:
    def reverse(self, x: 'int') -> 'int':
        stri = str(x)
        print("",stri)
        if x<0 and x>-2**31:
         
         if(stri[0]=="-"):
            li = stri.split('-')
            print("list",li)
            lirev= li[1]
            rev = lirev[::-1]
            rev = "-"+rev
            reverse_int = int(rev)
            if reverse_int<-2**31 or reverse_int>2**31:
                reverse_int=0
        elif x<2**31 and x>-2**31 and x>0:
            rev  = stri[::-1]
            reverse_int = int(rev)
            if reverse_int > 2**31:
                reverse_int=0
        else: 
            reverse_int=0
        return reverse_int
sol=Solution()
ans= sol.reverse(234)
print("",2**31)
print("",ans) 