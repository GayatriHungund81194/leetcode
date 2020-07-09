keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
arr = list()

for idx,j in enumerate(keyboard):
    arr.append((j,idx))
d = dict()
for i in range(len(arr)):
    if arr[i][0] not in d:
        d[arr[i][0]] = arr[i][1]
print(d)
sum = 0
prev = 0
for w in word:
    if d[w] > prev:
        sum = sum + d[w]
    elif d[w] < prev:
        sum = sum - d[w]
    else:
        sum = sum + 1
print(sum)

22 - 15 + 1 + 16 - 13 + 25 - 14 + 15