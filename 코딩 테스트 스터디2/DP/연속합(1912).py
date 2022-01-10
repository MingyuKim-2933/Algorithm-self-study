import sys
import math

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))


# DP를 적용하지 않으니 시간초과
# for i in range(n):
#     num_sum = 0
#     for j in range(i, n):
#         num_sum += li[j]
#         if num_sum > max:
#             max = num_sum

for i in range(0, n-1):
    if li[i] + li[i+1] > li[i+1]:
        li[i+1] = li[i] + li[i+1]

print(max(li))
