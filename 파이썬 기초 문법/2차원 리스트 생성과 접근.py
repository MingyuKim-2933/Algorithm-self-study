a = [0]*3  # 1차원 리스트 [0, 0, 0] 생성
print(a)

a = [[0]*3 for _ in range(3)]  # 2차원 리스트 생성 (2차원 리스트는 표를 연상하여 알고리즘 문제를 풀면 좋다.)
print(a)
a[0][1] = 1
print(a)
a[1][1] = 1
print(a)
print()

for x in a:  # 2차원 리스트를 표로 확인하는 법
    print(x)
print()

for x in a:  # 2차원 리스트의 원소들만 확인하는 법
    for y in x:
        print(y, end=' ')
    print()