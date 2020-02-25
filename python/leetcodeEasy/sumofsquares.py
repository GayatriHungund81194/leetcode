n = 4
l = list()
flag = 0
for i in range(1,n):
    if i*i < n:
        l.append(i)
print(l)

for i in range(len(l)):
    for j in range(1,len(l)):
        if (l[i]*l[i]) + (l[j]*l[j]):
            flag = 1
            print("true")
            
        else:
            print("false")