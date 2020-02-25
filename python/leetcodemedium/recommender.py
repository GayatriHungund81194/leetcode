products = ["mobile","mouse","moneypot","monitor","mousepad"]
products = sorted(products)
searchWord = "mouse"
l = list()
mainlist = list()
word = ""
for i in range(len(searchWord)):
    word = word + searchWord[i]
    for j in range(len(products)):
        
        #print("Word:",word)
        selectedword = products[j]
        #print("Selected Word:",selectedword[:i+1])
        if selectedword[:i+1] == word:
            if len(l)!=3:
                continue
            else:
                mainlist.append(l)
            l.append(selectedword)
            
    print(l)
    l.clear()
print(mainlist)