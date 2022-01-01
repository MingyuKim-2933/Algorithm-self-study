S = input()
a = []

for i in range(26):
    a.append(-1)
for i in range(26):
    temp = i+97
    for j in range(len(S)):
        if temp == ord(S[j]):
            a[i] = j
            break
    print(a[i], end=' ')