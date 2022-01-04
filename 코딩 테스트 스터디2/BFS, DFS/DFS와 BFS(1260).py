import sys
from collections import deque


def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(n):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1, n+1):
    graph[j].sort()

dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)
