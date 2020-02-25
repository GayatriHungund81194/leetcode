        # count = 0
        # i=0
        # flag= 0
        # l = list()
        # while i < len(T):
        #     for j in range(1,len(T)):
        #         if i < len(T):
        #             if T[j] > T[i]:
        #                 l.append(count+1)
        #                 count = 0
        #                 i = i + 1
        #             else:
        #                 count = count + 1
        # return l
arr = [73, 74, 75, 71, 69, 72, 76, 73]
i = 0 
j=1
count = 0 
flag = 0
day = list()
while i<len(arr):
    while j < len(arr):
        if arr[j] > arr[i]:
            if i == 0:
                day.append(1)
            else:
                day.append(count)
            print("Arr[i]:",arr[i])
            print("Arr[j]",arr[j])
            print("Count:",count)
            flag = 1
        else:
            count = count + 1
            j = j + 1
        
        if flag == 1:
            j = i + 1
            count = 0
            flag = 0
            break
    if j == len(arr):
        if arr[j-1] > arr[i]:
            day.append(1)
        else:
            day.append(0)
    i = i + 1
print(day)

    

