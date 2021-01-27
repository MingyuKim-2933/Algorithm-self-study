'''
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.
▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.
▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다.
▣ 입력예제 1
3
125 15232 97
▣ 출력예제 1
97
'''

N = int(input())
num = list(map(int, input().split()))  # 띄어쓰기로 구분된 입력을 각각 list에 추가한다.


def digit_sum():

    digit_sum = []
    temp1 = [0] * 8
    for i in range(len(num)):
        temp2 = 0
        for j in range(8):
            if int(num[i] / (10 ** (j + 1))) == int(num[i] / (10 ** j)):
                break
            temp1[j] = num[i] % (10 ** (j + 1))
            temp2 += int(temp1[j] / (10 ** j))  # 반올림 해줘야 자릿수가 나온다.
        digit_sum.append(temp2)
    return digit_sum.index(max(digit_sum))  # 인자로 받는 값의 인덱스를 반환한다.


print(num[digit_sum()])
