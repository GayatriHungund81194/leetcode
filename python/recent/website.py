from itertools import combinations 
from collections import defaultdict
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
l = list()
finalList = list()
userDict = defaultdict(list)
keyDict = dict()
for i in range(len(username)):
    l.append((username[i],timestamp[i],website[i]))
print(l)
for i in range(len(l)):
    userDict[username[i]].append(l[i][2])
for key in userDict:
    lis = userDict[key]
    perm = list(combinations(lis,3))
    finalList = finalList + perm
print(finalList)
count = 0
ll = list()
s = list(set(finalList))
for k in range(len(s)):
    s[k] = s[k] + (0,)
for k in range(len(s)):
    s[k] = list(s[k])
for i in range(len(s)):
    for j in range(len(finalList)):
        if finalList[j][0] == s[i][0] and finalList[j][1] == s[i][1] and finalList[j][2] == s[i][2]:
            s[i][3] = s[i][3] + 1
print(s)
