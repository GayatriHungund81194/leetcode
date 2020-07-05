import operator
str1 = "Aabb"
li = list()
ui = list()
str2 = sorted(str1)
print(str2)
sb = list()
sb.append(str2[0])
for i in range(1,len(str2)):
    if sb[0]==str2[i]:
        sb.append(str2[i])
    else:
        print(sb)
        st = "".join(sb)
        print(st)
        sb.clear()
        if st.isupper():
            ui.append(st)
        else:
            li.append(st)
        sb.append(str2[i])
if sb:
    print(sb)
    st = "".join(sb)
    if st.isupper():
        ui.append(st)
    else:
        li.append(st)
print(li)
print(ui)