def partitionLabels(S):
    last = dict()
    for i, c in enumerate(S):
        last[c] = i
    j = anchor = 0
    ans = []
    for i, c in enumerate(S):
        print("S",S)
        print("key",c)
        print("Last",last[c])
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
    print(ans)
S = "ababcbacadefegdehijhklij"
partitionLabels(S)