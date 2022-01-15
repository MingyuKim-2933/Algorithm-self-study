import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    li.append([s, e])

li.sort(key=lambda x: x[0])
li.sort(key=lambda x: x[1])

count = 1
end_time = li[0][1]
for i in range(1, n):
    if li[i][0] >= end_time:
        count += 1
        end_time = li[i][1]
print(count)
