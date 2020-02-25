num =10
l = list()
for i in range(1,num+1):
    if num % i == 0:
        l.append(i)
if len(l) > 2:
    print(l)
    print("Not prime")
else:
    print("Prime")
    print(l)