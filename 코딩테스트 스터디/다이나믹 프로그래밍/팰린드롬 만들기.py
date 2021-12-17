import sys

input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(reversed(arr1))
dp = [[0 for _ in range(n+1)]for _ in range(n+1)]
print(dp)
for i in range(n):
    for j in range(n):
        if arr1[i] == arr2[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
print(n-dp[n][n])
