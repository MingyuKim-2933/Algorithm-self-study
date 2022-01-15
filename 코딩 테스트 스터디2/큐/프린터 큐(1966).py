import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, doc = map(int, sys.stdin.readline().split())
    li = [i for i in range(n)]
    important = list(map(int, sys.stdin.readline().split()))

    queue = deque(list(zip(li, important)))

    answer = -1
    cnt = 0
    while answer != doc:
        im = queue[0][1]
        check = False
        for j in range(1, len(queue)):
            if im < queue[j][1]:
                queue.append(queue.popleft())
                check = True
                break
        if not check:
            temp = queue.popleft()
            cnt += 1
            answer = temp[0]
            check = False
    print(cnt)