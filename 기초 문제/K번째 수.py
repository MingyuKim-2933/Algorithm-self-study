T = int(input())
for t in range(T):
    N, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))  # 띄어쓰기로 구분되는 한 줄을 읽어와서 차례대로 리스트 값에 넣어준다.
    num = num[s-1:e].sort()
    print(num)
