# bfs풀이
from collections import deque
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


t = int(input())
result_list = []


def bfs(y, x):  # bfs를 사용한 풀이

    queue = deque([])
    queue.append([y, x])

    while queue:
        y, x = queue.pop()
        for d in range(4):
            xx = dx[d] + x
            yy = dy[d] + y
            if 0 <= xx < m and 0 <= yy < n:
                if graph[yy][xx] == 1:
                    graph[yy][xx] = 0
                    queue.append([yy, xx])


for _ in range(t):
    result = 0
    m, n, k = map(int, sys.stdin.readline().split()) # m:가로, n:세로
    graph = [[0] * m for _ in range(n)]
    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    for i in range(n): # 세로
        for j in range(m): # 가로
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1
    result_list.append(result)

for i in result_list:
    print(i)