import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
inDegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    arr.append([a, b])

for a, b in arr:
    inDegree[b] += 1
    graph[a].append(b)

for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()
    for j in graph[student]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            queue.append(j)
    print(student, end=' ')
