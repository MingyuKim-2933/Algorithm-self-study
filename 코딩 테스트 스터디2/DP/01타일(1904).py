import sys

n = int(sys.stdin.readline())

tile = [0] * 1000001

tile[1] = 1
tile[2] = 2
for i in range(3, n+1):  # 점화식을 구해봤을 때 피보나치 수열과 똑같은 규칙을 가지고 있다는 것을 알고 피보나치 수열로 해결함
    tile[i] = (tile[i-1] + tile[i-2]) % 15746

print(tile[n])
