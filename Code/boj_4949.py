while True:
    n = input()
    if n == '.':
        break

    stack = []

    for i in n:
        if i == '(' or i == '[':
            stack.append(i)
        if stack:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack[-1] == '[' and i == ')':
                stack.append(i)
            elif stack[-1] == '(' and i == ']':
                stack.append(i)
        else:
            if i == ')' or i == ']':
                stack.append(i)
    print("no" if stack else "yes")
