A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
finallist = list()
i = j = 0
while i < len(A) and j < len(B):
    start = max(A[i][0],B[j][0])
    end = min(A[i][1],B[j][1])
    if start <= end:
        finallist.append([start,end])
    if end == A[i][1]:
        i = i + 1
    else:
        j = j + 1
print(finallist)



        