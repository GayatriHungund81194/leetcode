st = "IX"
d = dict()
d = {"I":1,"V":5,"X":10,'L' : 50,"C" : 100,"D" : 500,"M" : 1000}
num = 0
for i in range(len(st)-1):
    st1 = d[st[i]]
    st2 = d[st[i+1]]
    if st1 >= st2:
        num = num + st1
    else:
        num  = num - st1
num = num + d[st[len(st)-1]]
print(num)

    
# for j in range(len(arr)):
#     if k<len(arr)-1:
#         if arr[j] < arr[k]:
#             num = num + arr[k] - arr[j]
#             k = k  + 2
#         else:
#             num = num + arr[k] + arr[j]
#             k = k  + 1
#     else:
#         num = num + arr[k-1]
# print(num)
            

