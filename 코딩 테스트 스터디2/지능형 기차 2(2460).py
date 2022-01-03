import sys

li = []
sum = 0
for i in range(10):
    a, b = map(int, sys.stdin.readline().split())
    li.append(sum - a)
    sum = sum - a
    li.append(sum + b)
    sum = sum + b
print(max(li))

'''
import sys

current=0
maxpass=0
for i in range(10):
    A,B=map(int,sys.stdin.readline().split())
    current-=A
    current+=B
    if maxpass<current : maxpass=current
print(maxpass)
'''