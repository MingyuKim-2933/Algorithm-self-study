import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    sentence = list(map(str, input().split()))
    for i in sentence:
        for j in range(len(i)-1, -1, -1):
            print(i[j], end='')
        print(' ', end='')

'''
import sys

for i in range(int(sys.stdin.readline())):
    # [::-1] 이걸로 입력한 단어로 reverse 
    # .split()으로 공백으로 구분하여 list로 쪼갬 
    word = sys.stdin.readline()[
           ::-1].split()  # ['yadot', 'yppah', 'ma', 'I'], ['ezirp', 'tsrif', 'eht', 'niw', 'ot', 'tnaw', 'eW']
    word.reverse()  # ['I', 'ma', 'yppah', 'yadot'] , ['eW', 'tnaw', 'ot', 'niw', 'eht', 'tsrif', 'ezirp']

    # " ".join(list) 로 단어들을 이어 붙임 
    print(' '.join(word))  # I ma yppah yadot , eW tnaw ot niw eht tsrif ezirp
'''
