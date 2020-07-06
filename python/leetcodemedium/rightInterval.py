intervals = [[3,4],[2,3],[1,2]]
ll = list()
l1 = list()
flag = 0
mini = 99999
idx = 0
for i in range(len(intervals)):
    for j in range(len(intervals)):
        if intervals[i][0] < intervals[j][0] and i!=j:
            if mini > intervals[j][1]:
                mini = intervals[j][1]
                idx = j
                flag = 1
    print("mini number",mini)
    print("min idx",idx)
    if flag!=1:
        l1.append(-1)
        flag = 0
    else:
        l1.append(idx)
        mini = 99999
        idx = 0
    #         l2.append(intervals[ll[i]][1])
    #     mini = 9999999
    #     idx = 0
    #     for i in range(len(l2)):
    #         if (l2[i]<mini):
    #             mini = l2[i]
    #             idx = i
    #     l1.append(idx)
    flag = 0
    print(l1)