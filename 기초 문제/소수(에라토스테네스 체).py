'''
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.
▣ 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
▣ 출력설명
첫 줄에 소수의 개수를 출력합니다.
▣ 입력예제 1
20
▣ 출력예제 1
8
'''


# count = 0
# N = int(input())
# for i in range(1, N+1):
#     divide = 0
#     for j in range(2, i+1):
#         if i % j == 0:
#             divide += 1
#     if divide == 1:
#         count += 1
# print(count)  # 답은 맞지만 Time Limit Exceeded


# My solution
N = int(input())
count = 0
temp = [1]+[0]*N
for i in range(2, N+1):
    if temp[i] == 0:
        count += 1
        for j in range(1, N):
            if i*j > N:
                break
            temp[i*j] = 1
print(count)

# Solution
# N = int(input())
# count = 0
# temp = [0]*(N+1)
# for i in range(2, N+1):
#     if temp[i] == 0:
#         count += 1
#         for j in range(i, N+1, i):
#             temp[j] = 1
# print(count)

