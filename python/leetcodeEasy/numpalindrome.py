class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        temp=x
        reverse=0

        while(x>0):
            dig=x%10
            reverse=reverse*10+dig
            x=x//10
            print("",reverse)
        if temp == reverse:
                return True
        else:
                return False

sol=Solution()
ans= sol.isPalindrome(232)
print("",ans) 