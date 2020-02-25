arr = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# flag = 0
# rowdict = dict()
# colDict = dict()
# for i in range(len(arr)):
#     aRow = arr[i]
#     if (aRow[i] not in rowdict and aRow[i]<10 and aRow[i]>0):
#         rowdict[i] = aRow[i]
#     else:
#         print("found duplication")

# for i in range(len(arr)):
#     aCol = [col[i] for col in arr]
#     if (aCol[i] not in colDict and aRow[i]<10 and aRow[i]>0):
#         colDict[i] = aCol[i]
#     else:
#         print("Duplicate found")

# #get 3*3
# smallMatrix = dict()
# count = 0
# smallMat = []
# for k in range(3):
#     for i in range(3):
#         firstRow = arr[i][:3]
#         smallMat[k] = firstRow
#         nextMat = arr[i][3:]
#         print(smallMat)
        # print(firstRow)
        # print(nextMat)
    # for j in range(len(firstRow)):
    #     if (firstRow[j] not in smallMatrix and firstRow[i]<10 and firstRow[i]>0):
    #         smallMatrix[j] = firstRow[j]
    #     else:
    #         print("Duplicate element")


# count = 0
# nextMat = []
# firstRow = []
# secondRow = []
# thirdRow = []
# nextMatOne = []
# nextMatTwo = []
# nextMatThree = []
# firstMat= []
# secondMat= []
# thirdMat = []
# for j in range(3):
#     for i in range(3):
#         if flag == 0:
#             firstRow = arr[count]
#             secondRow = arr[count+1]
#             thirdRow = arr[count+2]
#             firstMat = firstRow[:3]
#             secondMat = secondRow[:3]
#             thirdMat = thirdRow[:3]
#             nextMatOne = firstRow[3:]
#             nextMatTwo = secondRow[3:]
#             nextMatThree = thirdRow[3:]
#             flag = 1
#             print(firstRow)
#             print(secondRow)
#             print(thirdRow)
#         else:
#             firstRow = nextMatOne[:3]
#             secondRow = nextMatTwo[:3]
#             thirdRow = nextMatThree[:3]
#             nextMatOne = firstRow[3:]
#             nextMatTwo = secondRow[3:]
#             nextMatThree = thirdRow[3:]
#             print(firstRow)
#             print(secondRow)
#             print(thirdRow)
# print(arr)
flag= 0
row1 = []
row2 = []
row3 = []
nextRow1 = []
nextRow2 = []
nextRow3 = []
count = 0
for k in range(3):
    for i in range(3):
        if (flag == 0):
            row1 = arr[count][:3]
            row2 = arr[count+1][:3]
            row3 = arr[count+2][:3]
            count = count +  3
            nextRow1 = arr[i][3:]
            nextRow2 = arr[i+1][3:]
            nextRow3 = arr[i+2][3:]
            print(row1)
            print(row2)
            print(row3)
            # print(nextRow1)
            # print(nextRow1)
            # print(nextRow1)
            flag = 1
        else:
            print("$$$$$$$$$$$$$$$$")
            row1 = nextRow1[:3]
            row2 = nextRow2[:3]
            row3 = nextRow3[:3]
            print(row1)
            print(row2)
            print(row3)
            nextRow1 = nextRow1[3:]
            nextRow2 = nextRow2[3:]
            nextRow3 = nextRow3[3:]
    flag = 0







row_dict={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
col_dict={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
for i,v in enumerate(arr):
    for  index,j in enumerate(v):
        if j in row_dict[i] and j.isdigit():
            print("duplicate")
        row_dict[i].append(j)
        if j in col_dict[i] and j.isdigit():
            print("duplicate")
        col_dict[index].append(j)