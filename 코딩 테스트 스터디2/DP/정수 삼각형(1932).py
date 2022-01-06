import sys

n = int(sys.stdin.readline())
point = []
count = 0
for i in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    temp = []
    for n, v in enumerate(li):
        if point:
            if n == 0:
                temp.append(v + point[i-1][0])
            elif n == (len(li) - 1):
                temp.append(v + point[i-1][-1])
            else:
                temp.append(v + point[i-1][n-1])
                temp.append(v + point[i-1][n])
        else:
            point.append([v])
    if i >= 1:
        point.append(temp)
print(point)
print(max(max(point)))
