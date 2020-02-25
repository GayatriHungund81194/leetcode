l = [1,2,3,4,5,6,7,8]
def binsrch(key,l,r,arr):
    mid = int(l + (r-1)/2)
    if key == arr[mid]:
        print("found at:",mid)
    elif arr[mid] > key:
        return binsrch(key,l,mid-1,arr)
    elif arr[mid] < key:
        return binsrch(key,mid+1,r,arr)
binsrch(3,0,8,l)