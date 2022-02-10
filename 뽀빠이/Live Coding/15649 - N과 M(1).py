import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

li = [i+1 for i in range(N)]

sequence = list(permutations(li, M))

for i in sequence:
    for j in i:
        print(j, end=' ')
    print()
