list = []
for i in range(9):
    list.append(int(input()))

total = sum(list)

for i in range(9):
    for j in range(i + 1, 9):
        if total - list[i] - list[j] == 100:
            del list[i]
            del list[j - 1]
            list.sort()
            break

    if len(list) < 9:
        break

for i in range(len(list)):
    print(list[i])