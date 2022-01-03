N = int(input())
score = list(map(int, input().split()))
M = 0
avg = 0

for i in range(N):
    if score[i] >= M:
        M = score[i]
for j in range(N):
    avg += score[j] / M * 100 / N
print(avg)