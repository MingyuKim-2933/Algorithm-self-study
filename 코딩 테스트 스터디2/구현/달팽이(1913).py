import sys
n = int(sys.stdin.readline())
num = int(sys.stdin.readline())

graph = [[0 for _ in range(n)] for _ in range(n)]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 이동할 수 있는 경우의 수를 모두 선언한다.

x = 0
y = 0
d = 0
find_x = 0
find_y = 0

for i in range(n*n, 0, -1):
    graph[y][x] = i
    if x + move[d][0] < 0 or x + move[d][0] >= n or y + move[d][1] < 0 or y + move[d][1] >= n or graph[y+move[d][1]][x+move[d][0]] != 0:  # 이동한 좌표가 0 미만 n 이상 그리고 이미 graph 안에 숫자가 채워져 있으면 방향을 바꿔준다.
        d = (d + 1)
        if d > 3:
            d = d - 4
    y = y + move[d][1]
    x = x + move[d][0]

for i in range(n):
    if num in graph[i]:  # graph의 한 줄마다 탐색하면서 만약 그래프 안에 찾고자 하는 자연수가 있다면 그 인덱스를 반환한다.
        find_y = i+1
        find_x = graph[i].index(num)+1

for i in graph:
    for j in i:
        print(j, end=' ')
    print()

print(find_y, find_x)

