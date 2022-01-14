import sys

t = int(sys.stdin.readline())

for i in range(t):
    string = sys.stdin.readline().strip()
    li = []
    for j in string:
        li.append(j)
        if len(li) >= 2:
            if li[-1] == ')' and li[-2] == '(':
                del li[-1]
                del li[-1]
    if not li:
        print("YES")
    else:
        print("NO")
