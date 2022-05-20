from collections import Counter
import sys

a, b = map(int, sys.stdin.readline().split())
answer = 0
first = list(set(map(int, input().split())))
second = list(set(map(int, input().split())))

union = first + second
values = Counter(union).values()

for i in values:
    if i <= 1:
        answer += 1

print(answer)
