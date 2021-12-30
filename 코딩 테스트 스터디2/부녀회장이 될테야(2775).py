import sys
input = sys.stdin.readline
t = int(input())
li = [[],[]]


for i in range(t):
    k = int(input())
    n = int(input())
    li[0].append(k)
    li[1].append(n)

apart = [[i+1 for i in range(max(li[1]))]]
for i in range(max(li[0])):
    apart.append([0] * max(li[1]))
for i in range(1, len(apart)):
    for j in range(max(li[1])):
        if j >= 1:
            apart[i][j] = apart[i-1][j] + apart[i][j-1]
        else:
            apart[i][j] = apart[i-1][j]

for i in range(t):
    print(apart[li[0][i]][li[1][i] - 1])

'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    people = [i for i in range(n + 1)]

    for i in range(k):
        for j in range(1, n + 1):
            people[j] = people[j] + people[j - 1]

    print(people[-1])
'''