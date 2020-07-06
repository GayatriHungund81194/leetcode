A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
left = 0
start = 0
right = 1
for i in range(len(A)):
    for j in range(start,len(A)):
        if A[j] == 0:
            K = K - 1
    if K < 0:
        start = start + 1
print(start)
