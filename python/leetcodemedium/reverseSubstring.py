s = "(u(love)i)"
stack = [[]]
for ch in s:
    if ch == '(':
        stack.append([])
    elif ch == ')':
        word = stack.pop()
        stack[-1].extend(word[::-1])
    else:
        stack[-1].append(ch)
st = "".join(stack.pop())
print(st)