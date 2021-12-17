import sys
from collections import deque
n = int(sys.stdin.readline())

queue = deque()
dist = [0] * (n+1)

for i in range(2, n+1):
    dist[i] = dist[i-1] + 1
    if i % 3 == 0 and dist[i] > dist[i//3] + 1:
        dist[i] = dist[i//3] + 1
    if i % 2 == 0 and dist[i] > dist[i//2] + 1:
        dist[i] = dist[i//2] + 1
print(dist[n])
