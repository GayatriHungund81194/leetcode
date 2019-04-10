arr = [9,8,7,6,5,4,3]

#With 3rd variable
# temp=0
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if j<len(arr):
#             if arr[i]<arr[j]:
#                 temp=arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=temp
# print(arr)

#without 3rd variable
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[i]<arr[j]:
            arr[i] = arr[i]+arr[j]
            arr[j] = arr[i]-arr[j]
            arr[i] = arr[i]-arr[j]
print(arr)