# pushed = [1,2,3,4,5]
# popped = [4,5,3,2,1]
# pushed = [1,2,3,4,5]
# popped = [4,3,5,1,2]
pushed = [0,2,1]
popped = [0,1,2]
j = 0
stack = []
for x in pushed:
    stack.append(x)
    while stack and j < len(popped) and stack[-1] == popped[j]:
        stack.pop()
        j += 1
    

