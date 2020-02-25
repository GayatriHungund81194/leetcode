class binarySearch:
    def  __init__(self,arr):
        self.arr = arr
    
    def binsearch(self,arr,left,right,key):
        if right >= left:
            mid = int((left + (right-1))/2)

        if arr[mid]==key:
            return mid

        elif arr[mid] > key:
            return self.binsearch(arr,left,mid-1,key)
        elif arr[mid] < key:
            return self.binsearch(arr,mid+1,right,key)

if __name__ == "__main__":
    arr = [2,5,8,12,16,23,28,56,72,91]
    bs = binarySearch(arr)
    index = bs.binsearch(arr,0,len(arr)-1,72)
    print(index)


        

        