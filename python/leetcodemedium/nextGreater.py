ll = [1,7,5,1,9,2,5,1]
l1 = list()
flag = 0
numdict = dict()
for i in range(len(ll)):
    for j in range(i+1,len(ll)):
        if ll[i]<ll[j]:
            l1.append(ll[j])
            flag = 1
            break
    if flag == 0:
        l1.append(0)
    else:
        flag = 0
print(l1)