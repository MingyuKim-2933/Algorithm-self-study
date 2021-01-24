'''
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
▣ 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
▣ 출력설명
첫 번째 줄에 답을 출력합니다.
▣ 입력예제 1
4 6
▣ 출력예제 1
5 6 7
'''

N, M = map(int, input().split())
count=[]
for i in range(N*M):
    count.append(0)
for i in range(1, N+1):
    for j in range(1, M+1):
        count[i+j] += 1
for i in range(len(count)):
    if count[i] == max(count):
        print(i, end=' ')

'''
N, M = map(int, input().split())
count = [0] * (n+m+3)  # n+m = 합의 최댓값 - for문보다 효율적
max =-21470000
for i in range(1, N+1):
    for j in range(1, M+1):
        count[i+j] += 1
for i in range(n+m+1):
    if count[i] > max:
        max=count[i]
for i in range(n+m+1):
    if count[i] == max:
        print(i, end=' ')
'''