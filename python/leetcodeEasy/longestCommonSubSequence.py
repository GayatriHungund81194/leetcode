class Solution(object):
    
    def longestCommonPrefix(self, strs):
        resultLen = len(strs[0])
        result=list()
        for x in range(1,len(strs)):
            smalleln = len(strs[x])
            if resultLen > smalleln:
                resultLen = smalleln
                resultStr = strs[x]
                
        for z in range(len(strs)):
            for y in range(len(resultStr)):
                compStr = strs[z]
                if resultStr[y] == compStr[y] and resultStr!=compStr:
                    print("",resultStr[y])
                    result = result + compStr[y]
            


        return result


sol=Solution()
l = ["flower","flow","flight"]
ans= sol.longestCommonPrefix(l)
print("",ans) 