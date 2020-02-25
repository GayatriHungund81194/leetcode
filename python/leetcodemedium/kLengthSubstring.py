st = "havefunonleetcode"
count = 0
finalarr = list()
for i in range(0,len(st)): 
    print(st[i:count+5])
    if len(st[i:count+5]) == len(set(st[i:count+5])) and len(st[i:count+5]) == 5:
        finalarr.append(st[i:count+5])
    count = count+1
print(finalarr)
