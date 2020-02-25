arr = [17,18,5,4,6,1]
dict1 =dict()
arr1 = []
for i in range(len(arr)):
    dict1.setdefault(arr[i],list(arr[i+1:]))

for key in dict1:
    if not dict1[key]:
        dict1[key].append(-1)
print(dict1)
for key in dict1:
    arr1.append(max(dict1[key]))
print(arr1)