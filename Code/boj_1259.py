while True:
    n = input()
    if n == '0':
        break
    check = True
    for i in range(len(n)):
        if n[i] != n[len(n) - i - 1]:
            check = False

    print("yes" if check else "no")