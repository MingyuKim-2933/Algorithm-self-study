import sys
from itertools import permutations
n, m = map(int,sys.stdin.readline().split())

li = [i for i in range(1, n+1)]

nums = list(permutations(li, m))

for i in nums:
    for j in i:
        print(j, end=' ')
    print()