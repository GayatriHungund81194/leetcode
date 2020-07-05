class Solution:
    
        
    def romanToInt(self, s: 'str') -> 'int':
        

        integer = 0
        x=0
        x2=0
        val=0
        val2=0
        while x < len(s):
            sym = s[x]
            sym2 = s[x+1]
            if sym == 'I':
                val = 1
            elif sym == 'V':
                val = 5
            elif sym == 'X':
                val = 10
            elif sym == 'L':
                val = 50
            elif sym == 'C':
                val = 100
            elif sym == 'D':
                val = 500
            elif sym == 'M':
                val = 1000
            else:
                val= -1

            if sym2 == 'I':
                val2 = 1
            elif sym2 == 'V':
                val2 = 5
            elif sym2 == 'X':
                val2 = 10
            elif sym2 == 'L':
                val2 = 50
            elif sym2 == 'C':
                val2 = 100
            elif sym2 == 'D':
                val2 = 500
            elif sym2 == 'M':
                val2 = 1000
            else:
                val2 = -1

            if val2>=val:
                resultVal=val2+val
                x = x+1

            else:
                resultVal = resultVal+ val2-val
                x = x+2

            
        return resultVal

    
            
sol=Solution()
ans= sol.romanToInt('IV')
print("",ans) 
