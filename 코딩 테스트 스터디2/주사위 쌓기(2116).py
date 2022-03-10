import sys

n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

route = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
max_num = 0

for i in range(6):
    result = []
    tmp = [1, 2, 3, 4, 5, 6]
    tmp.remove(array[0][i])
    next = array[0][route[i]]
    tmp.remove(next)
    result.append(max(tmp))
    for j in range(1, n):
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.remove(next)
        next = array[j][route[array[j].index(next)]]
        tmp.remove(next)
        result.append(max(tmp))
    result = sum(result)
    if max_num < result:
        max_num = result

print(max_num)