import sys

n = int(sys.stdin.readline())
graph = []
score = [1] * n

for i in range(n):
    w, h = map(int, sys.stdin.readline().split())
    graph.append([w, h])

for i in range(n):
    for j in range(i+1, n):
        if graph[i][0] < graph[j][0] and graph[i][1] < graph[j][1]:
            score[i] += 1
        elif graph[i][0] > graph[j][0] and graph[i][1] > graph[j][1]:
            score[j] += 1


for i in score:
    print(i, end=' ')