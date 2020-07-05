T = [55,38,53,81,61,93,97,32,43,78]
cnt =1
flag= 0
li = list()
ptr1 = 0
ptr2 = 1
for k in range(len(T)):
    for i in range(k+1,len(T)):
        if T[i] > T[k]:
            li.append(cnt)
            cnt = 1
            flag = 1
            break
        
        cnt = cnt + 1
        print("List",li)
    if flag == 1:
        flag = 0
    else:
        li.append(0)
        cnt = 1
    print("List",li)