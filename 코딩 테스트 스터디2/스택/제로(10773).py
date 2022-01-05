import sys

k = int(sys.stdin.readline())
queue = []
for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        queue.pop()
    else:
        queue.append(num)

print(sum(queue))