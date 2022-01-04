import sys

n, m = map(int, sys.stdin.readline().split())
board = []
count = []

for _ in range(n):
    board.append(sys.stdin.readline())

for a in range(n-7):
    for b in range(m-7):
        idx1 = 0
        idx2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        idx1 += 1
                    if board[i][j] != 'B':
                        idx2 += 1
                else:
                    if board[i][j] != 'B':
                        idx1 += 1
                    if board[i][j] != 'W':
                        idx2 += 1
        count.append(min(idx1, idx2))

print(min(count))