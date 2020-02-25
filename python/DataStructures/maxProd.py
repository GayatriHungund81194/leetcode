arr = [-2,0,-1]
initLen = len(arr)
count = 0
arr2 = []
maxProd = 0
prod = 1
while count!= initLen:
    arr = arr[count:]
    for i in range(len(arr)+1):
        arr2 = arr[:i]
        print(arr2)

        for i in range(len(arr2)):
            prod = prod * arr2[i]
            print("Product",prod)
        if (prod>maxProd):
            maxProd = prod
            print("Product",prod)
        prod = 0
    count = count + 1
    print(maxProd)
        

