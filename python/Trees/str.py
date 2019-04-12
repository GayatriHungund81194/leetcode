
strlist = list()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com"]
count=0
for email in emails:
    st =email.split('@')
    st[1] = '@'+st[1]
    if '.' in st[0]:
        s=st[0].replace('.','')
        st[0]=s
        print(st[0])
        if '+' in st[0]:
            s2 = st[0].split('+')
        st[0]=s2[0]
    emails[count] = "".join(st)
    count = count+1
print(emails)
