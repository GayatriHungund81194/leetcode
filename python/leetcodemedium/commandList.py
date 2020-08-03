s = "deeedbbcccbdaa"
k = 3
arr = list(s)
prev = ""
cnt = 0
idxlist = list()
for i in range(len(s)):
    if s[i] == prev:
        cnt +=1
        idxlist.append(i)
    if cnt==2:
        for j in range(len(idxlist)):
            arr[idxlist[j]-1] = "."
        arr[idxlist[-1]] = "."
        cnt = 0
        del idxlist[:]
    if s[i]!=prev:
        cnt = 0
        del idxlist[:]
    prev = s[i]
print("".join(arr))
