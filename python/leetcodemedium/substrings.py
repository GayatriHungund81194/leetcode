st = "abc"
stlist = list()
pallist = list()
for i in range(len(st)):
    for j in range(i+1,len(st)+1):
        stlist.append(st[i:j])
print(stlist)
for i in range(len(stlist)):
    st = stlist[i]
    if st == st[::-1]:
        pallist.append(st)
print(pallist)
