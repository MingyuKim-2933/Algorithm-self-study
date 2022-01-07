import sys

n = sys.stdin.readline().strip()
cnt = 0
for i in range(len(n)):
    if i >= 1:
        if n[i] != n[i-1]:  # 문자가 바뀔 때만 count + 1
            cnt +=1
print((cnt+1)//2)