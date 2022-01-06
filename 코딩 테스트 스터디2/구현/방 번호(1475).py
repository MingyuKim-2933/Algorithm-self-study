import sys

n = sys.stdin.readline().strip()

li = [0] * 10

for i in n:
    if i == '6' or i == '9':
        li[6] += 0.5
    else:
        li[int(i)] += 1

if str(max(li)).isnumeric():  # 문자열 안의 모든 문자가 정수면 True 아니면 False
    print(max(li))
else:
    print(int(max(li)+0.5))