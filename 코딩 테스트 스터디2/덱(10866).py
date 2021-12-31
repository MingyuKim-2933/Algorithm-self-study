from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline().strip()

    if a.find("push_front") != -1:
        push, num = a.split()
        queue.insert(0, num)

    elif a.find("push_back") != -1:
        push, num = a.split()
        queue.append(num)

    elif a == "pop_front":
        if not queue:
            print("-1")
        else:
            print(queue.popleft())

    elif a == "pop_back":
        if not queue:
            print("-1")
        else:
            print(queue.pop())

    elif a == "size":
        print(len(queue))

    elif a == "empty":
        if not queue:
            print("1")
        else:
            print("0")

    elif a == "front":
        if not queue:
            print("-1")
        else:
            print(queue[0])

    elif a == "back":
        if not queue:
            print("-1")
        else:
            print(queue[-1])
