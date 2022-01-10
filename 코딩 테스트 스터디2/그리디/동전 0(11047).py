import sys

n, k = map(int, sys.stdin.readline().split())
li = []
count = 0
for i in range(n):
    li.append(int(sys.stdin.readline()))

for i in range(len(li)-1, -1, -1):
    if k / li[i] >= 1:
        count += k // li[i]
        k = k % li[i]

print(count)
