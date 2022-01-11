def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
print(graph)
visited = [False] * (n+1)

for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

cnt = -1
for i in visited:
    if i:
        cnt += 1

print(cnt)
