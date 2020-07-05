logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
d = dict()
lis = list()
diglist = list()
for i in range(len(logs)):
    if "let" in logs[i]:
        l = logs[i].split(" ")
        d[l[0]] = " ".join(l[1:])
    else:
        diglist.append(logs[i])
for key in d:
    lis.append(d[key])
lis.sort()
for key,val in enumerate(d):
    if 
