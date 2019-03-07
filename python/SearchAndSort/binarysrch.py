def binsrch(arr,left,right,x):
    if right >= 1:
        mid = int(1 + (right-left)/2)

        if arr[mid] == x:
            return mid

        if arr[mid]>x:
            binsrch(arr,left,mid-1,x)

        else:
            binsrch(arr,mid+1,right,x)
    else: 
        return -1
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
result = binsrch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print("Element is present at index ",result) 
else: 
    print("Element is not present in array")