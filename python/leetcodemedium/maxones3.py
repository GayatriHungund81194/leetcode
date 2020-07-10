maxconsone = 0
left = 0
right  = 0
zcount = 0
A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
for right in range(len(A)):
    if A[right] == 0:
        zcount = zcount + 1
    while zcount > K:
        if A[left] == 0:
            zcount = zcount - 1
        left = left + 1
    maxconsone = max(maxconsone,right-left+1)
print(maxconsone)

