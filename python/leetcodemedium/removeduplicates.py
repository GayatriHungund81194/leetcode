s = "abcd"
k = 2
i=0
while i<len(s):
    if s[i:i+k]==s[i]*k:
        s=s[:i]+s[i+k:]
        i=0
    else:
        i+=1