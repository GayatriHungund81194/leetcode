st = "leelcode"
lis = list()
for i in range(len(st)):
    if len(lis) == 0:
        lis.append(st[i])
    else:
        elem = lis[-1]
        if elem == st[i]:
            lis.pop()
            print(lis)
        else:
            lis.append(st[i])
st = "".join(lis)