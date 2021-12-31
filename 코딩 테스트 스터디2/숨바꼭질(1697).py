from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n)
dist = [0] * 100001
while q:
    x = q.popleft()
    if x == k:
        print(dist[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0 <=nx <= 100000 and not dist[nx]:
            dist[nx] = dist[x] + 1
            q.append(nx)