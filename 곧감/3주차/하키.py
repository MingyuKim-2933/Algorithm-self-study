import sys


def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5


W, H, X, Y, P = map(int, sys.stdin.readline().split())

X_max = X + W
Y_max = H + Y
answer = 0
for i in range(P):
    px, py = map(int, sys.stdin.readline().split())
    if X <= px <= X_max and Y <= py <= Y_max:
        answer += 1
        continue

    r = H/2
    if get_distance(X, Y+r, px, py) <=r or get_distance(X_max, Y+r, px,py) <= r:
        answer += 1

print(answer)
