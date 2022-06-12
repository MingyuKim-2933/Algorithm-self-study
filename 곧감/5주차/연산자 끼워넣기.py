import sys

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

plus, minus, multi ,divide = map(int, sys.stdin.readline().split())

maximum = -1e+8
minimum = 1e+8


def dfs(depth, total, plus, minus, multi, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + li[depth], plus - 1, minus, multi, divide)
    if minus:
        dfs(depth + 1, total - li[depth], plus, minus - 1, multi, divide)
    if multi:
        dfs(depth + 1, total * li[depth], plus, minus, multi - 1, divide)
    if divide:
        dfs(depth + 1, int(total / li[depth]), plus, minus, multi, divide - 1)


dfs(1, li[0], plus, minus, multi, divide)

print(maximum)
print(minimum)
