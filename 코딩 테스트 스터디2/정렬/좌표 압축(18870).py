import sys
n = int(sys.stdin.readline())

point = list(map(int, sys.stdin.readline().split()))

sorted_point = sorted(list(set(point)))

dic = {sorted_point[i]:i for i in range(len(sorted_point))}

for i in point:
    print(dic[i], end=' ')