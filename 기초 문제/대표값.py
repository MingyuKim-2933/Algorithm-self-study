'''
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연
수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.
▣ 입력예제 1
10
45 73 66 87 92 67 75 79 75 80
▣ 출력예제 1
74 7
'''

N = int(input())
score = list(map(int, input().split()))
avg = sum(score) / N
avg_check = avg % 1
if 0.5 <= avg_check < 1:
    avg = avg + 1
avg = int(avg)
compare = []
num = []

for i in range(N):
    if avg-score[i] >= 0:
        compare.append(avg - score[i])
    else:
        compare.append(score[i] - avg)

min = 100

for i in range(len(compare)):
    if min == compare[i]:
        if score[i] > score[out]:
            out = i
    if min > compare[i]:
        min = compare[i]
        out = i
out = out + 1
print(avg, out)
