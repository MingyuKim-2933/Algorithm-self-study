import sys

t = int(sys.stdin.readline())

dp = [0, 1, 2, 4]
k = 4
case = []
for i in range(t):
    case.append(int(sys.stdin.readline()))

while k <= max(case):
    dp.append(dp[k-1] + dp[k-2] + dp[k-3])
    k += 1

for i in case:
    print(dp[i])