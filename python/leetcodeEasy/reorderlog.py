lettlogs = []
digitlogs = []
logs1 = list()
identifier = ""
combinedStr = ""
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
for log1 in logs:
    log = log1.split(" ",1)
    if "dig" in log[0]:
        digitlogs.append(log1)
    else:
        lettlogs.append(log1)
print("Digit:",digitlogs)
print("Letter:",lettlogs)

# lettDict = dict()
# for lettlog in lettlogs:
#     lettlog1 = lettlog.split(" ",1)
#     lettDict[lettlog1[0]] = lettlog1[1]
# for i in sorted (lettDict.values()) :  
#     print(i, end = " ") 
sorted(lettlogs)
print(lettlogs)


