def gcd(a, b):
    b = gcd(b, a % b) if b else a
    return b


print(gcd(38, 18))


# def extended_gcd(a, b):
#     r0, r1 = a, b
#     s0, s1 = 1, 0
#     t0, t1 = 0, 1
#
#     while r1:
#         q = r0 // r1
#         r0, r1 = r1, r0 - r1 * q
#         s0, s1 = s1, s0 - s1 * q
#         t0, t1 = t1, t0 - t1 * q
#
#     return r0, s0, t0
