def fastsum(n) -> int:
    if n == 1:
        return 1
    if n % 2 == 1:
        return fastsum(n-1) + n
    else:
        return n**2 // 4 + 2 * fastsum(n//2)

print(fastsum(100))