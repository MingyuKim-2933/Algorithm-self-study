'''
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가
여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려
고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력
하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값
은 22입니다.
▣ 입력설명
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력
된다.
▣ 출력설명
첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.
▣ 입력예제 1
10 3
13 15 34 23 45 65 33 11 26 42
▣ 출력예제 1
143
'''

N, K = map(int, input().split())
num = list(map(int, input().split()))
num.sort(reverse=True)
num_sum = []

for i in range(len(num)):
    for j in range(i+1, len(num)):
        for k in range(j+1, len(num)):
            num_sum.append(num[i]+num[j]+num[k])
set = set(num_sum)  # set을 사용하여 중복을 제거하였다.
num_sum = list(set)  # 만약 sort가 되어있는 상태여도 set함수를 사용하면 순서가 뒤죽박죽 되어 다시 sort 해주어야 한다.
num_sum.sort(reverse=True)
print(num_sum[K-1])
