def climbStairs(i, n):
    if i == n:
        return 1
    if i > n:
        return 0
    return climbStairs(i+1,n) + climbStairs(i+2,n)

s = climbStairs(0,4)
print(s)
