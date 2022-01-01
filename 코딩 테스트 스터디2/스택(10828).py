import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    a = sys.stdin.readline().strip()

    if a.find("push") != -1:
        push, num = a.split()
        stack.append(int(num))

    elif a == "top":
        if not stack:
            print("-1")
        else:
            print(stack[-1])
    elif a == "size":
        print(len(stack))
    elif a == "empty":
        if not stack:
            print("1")
        else:
            print("0")
    elif a == "pop":
        if not stack:
            print("-1")
        else:
            print(stack.pop())

'''
import sys

stack = list()

command = dict(
    push=lambda x: stack.append(x),
    pop=lambda: stack.pop() if stack else -1,
    size=lambda: len(stack),
    empty=lambda: 0 if stack else 1,
    top=lambda: stack[-1] if stack else -1
    )

in_data = sys.stdin.readlines()
for c in in_data[1:]:
    c = c.strip()
    if c[:2] == 'pu':
        command['push'](c.split()[1])
    else:
        print(command[c]())
'''