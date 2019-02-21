if __name__ == '__main__':
    S = [1,2,3,5,3]
    E = [5,5,7,6,10]
    chairMap = dict()
    tup=list(zip(S,E))
    ll =sorted(tup)
    print("Sorted list: O(nlogn):",ll)
    print("Max Chairs we can have: ",len(ll))
    chairs = len(ll)
    for x in range(chairs):
        chairMap[x]=0
    print("Initially Chairs allocated:",chairMap)
    for x in range(len(ll)):
        for y in range(x,len(ll)):
            if x == 0:
                chairs=chairs-1
                chairMap[x]=1
            elif ll[y][0]<ll[x][1]  and chairMap[y]!=1:
                chairMap[y]=1
                chairs = chairs -1
            elif ll[x][1]<=ll[y][1] and ll[y][0]>ll[x][1] and chairMap[y]!=1:
                chairMap[y]=1
                chairs = chairs-1
            elif ll[y][0]>=ll[x][1] and chairMap[x]==1:
                chairMap[x]=0
                chairMap[y]=1

            # if ll[x][1]>=ll[y][1] and chairMap[x]!=1:
            #     print("",ll[x][1])
            #     print("",ll[y][1])
            #     chairs = chairs-1
            #     chairMap[x]=1
    print("After Allocation:",chairMap)
    print("Chairs:",chairs)


