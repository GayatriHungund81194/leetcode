
def binsrch(arr,l,r,x):
    if (r>=l):
        mid = int(l+(r-l)/2)

        if (x==arr[mid]):
            return mid
        elif (x<arr[mid]):
            return binsrch(arr,1,mid-1,x)
        else:
            return binsrch(arr,mid+1,r,x)
    else: 
        return -1

if __name__=="__main__":
    x=6
    arr = [2,3,4,5,6]
    result = binsrch(arr, 0, len(arr)-1, x) 
    print("Index:",result)
