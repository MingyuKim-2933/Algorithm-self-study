import sys

input = sys.stdin.readline
t = int(input())
for i in range(t):
    num = int(input())
    bi = bin(num)
    bi = bi[2:]
    count = 0
    for i in range(len(bi)-1, -1, -1):
        if bi[i] == '1':
            print(count, end= " ")
        count += 1