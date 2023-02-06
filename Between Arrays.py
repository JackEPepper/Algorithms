from functools import reduce

def __gcd(a, b):
    return a if b == 0 else __gcd(b, a%b)

def array_gcd(arr):
    return reduce(__gcd, arr)

def array_lcm(arr):
    lcm = 1
    for i in arr:
        lcm = lcm * i // __gcd(lcm, i)
    return lcm

def BetweenArraysCount(a, b):
    lcm = array_lcm(a)
    gcd = array_gcd(b)
    return sum(True for i in range(lcm, gcd+1, lcm) if gcd % i == 0)

print(BetweenArraysCount(list(range(2,5,2)), list(range(16,17*4,16))))