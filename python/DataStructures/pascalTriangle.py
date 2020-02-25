l = list()
m = []
for i in range(1,6):
    random = 1
    m.clear()
    for j in range(1,i+1):
        m.append(random)
        random = random*(i+j)/j
    l.append(m)
    print(l)
