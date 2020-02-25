arr = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
peremeter = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] is 1:
            if arr[i][j-1] is 0:
                peremeter = peremeter + 1
            if arr[i][j+1] is 0:
                peremeter = peremeter + 1
            if i+1 < len(arr):
                if arr[i+1][j] is 0:
                    print("Down Row:",i)
                    peremeter = peremeter + 1
            if i-1 >= 0 :
                if arr[i-1][j] is 0:
                    print("Up Row:",i)
                    peremeter = peremeter + 1
            if i+1 == len(arr) or i-1 < 0:
                peremeter = peremeter + 1
print(peremeter)

