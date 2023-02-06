from functools import reduce

def __gcd(a, b): # Gets GCD of two numbers
    return a if b == 0 else __gcd(b, a%b)

def array_gcd(arr): # Gets GCD of an arbitrarily long array
    return reduce(__gcd, arr)

def array_lcm(arr): # Computes LCM of arbitrarily long array
    lcm = 1
    for i in arr:
        lcm = lcm * i // __gcd(lcm, i)
    return lcm

def BetweenArraysCount(a, b): # Computes how many numbers are multiples of all elements of A that are also factors of all elements of B
    lcm = array_lcm(a)
    gcd = array_gcd(b)
    return sum(True for i in range(lcm, gcd+1, lcm) if gcd % i == 0) # Counts the multiples of the LCM of array A that perfectly divide the GCD of array B

print(BetweenArraysCount(list(range(2,5,2)), list(range(16,17*4,16))))