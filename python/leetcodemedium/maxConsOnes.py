A = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
left = 0
count = 0
maxcount = 0
for right in range(len(A)):
    if A[right] == 0:
        k = k - 1
        if k <= 0:
            if maxcount < count:
                maxcount = count
                count = 0
    count  = count + 1
print(maxcount)

