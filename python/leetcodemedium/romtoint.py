s = "IX"
n = len(s)
r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
sum = 0
for i in range(n-1):
    v1 = r[s[i]]
    print("V1:",v1)
    v2 = r[s[i+1]]
    print("V2:",v2)
    if v1 >= v2:
        sum += v1
        print("Sum;",sum)
    else:
        sum -= v1
        print("Sum:",sum)

print(sum + r[s[-1]])