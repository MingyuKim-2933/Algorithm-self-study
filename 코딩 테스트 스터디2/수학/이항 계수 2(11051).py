import sys


def factorial(num):
    fac_num = 1
    for i in range(1, num+1):
        fac_num = fac_num * i
    return fac_num


n, k = map(int, sys.stdin.readline().split())

print(((factorial(n) // (factorial(k) * factorial(n-k))) % 10007))