# Brute Force Algorithm
def get_gcd_using_BF(a, b):
    min_num = min(a, b)
    for i in range(1, min_num+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


# Euclidean Algorithm Using Loops
def get_gcd_using_EA_loops(a, b):
    # b를 큰값으로 두기 위한 코드
    if a > b:
        tmp = a
        a = b
        b = tmp

    while a != 0:
        n = b % a
        b = a
        a = n

    return b


# Euclidean Algorithm Using Recursion
def get_gcd_using_EA_recursion(a, b):
    if a % b == 0:
        return b
    else:
        return get_gcd_using_EA_recursion(b, a % b)


def get_lcm(a, b):
    return int(a * b / get_gcd_using_EA_recursion(a, b))


import math

# a, b는 임의의 두 자연수

#math.gcd는 파이썬 3.5 버전 이상일 때 사용가능
math.gcd(a, b)

#math.lcm은 파이썬 3.9 버전 이상일 때 사용가능
math.lcm(a, b)
