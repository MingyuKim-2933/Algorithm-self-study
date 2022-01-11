import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())

li = list(map(str, sys.stdin.readline().split()))
# toggle = True  # 조합을 사용하면 필요없는 코드
li.sort()
li = list(combinations(li, L))  # permutations(순열)로 했을 때 메모리 초과가 발생
for i in li:
    vo_cnt = 0
    co_cnt = 0
    for j in range(len(i)):
        if i[j] in "aeiou":  # 모음이 있으면 카운트 추가
            vo_cnt += 1
        else:  # 자음일 때 카운트 추가
            co_cnt += 1
        '''
        if j >= 1 and i[j] < i[j-1]:  # combinations를 쓰면 AB AC AD BC BD CD 순으로 조합을 반환하기에 이 조건문이 필요없다.
            toggle = False
            break
        '''

    if vo_cnt >= 1 and co_cnt >= 2:
        print("".join(i))
    # toggle = True  # 조합을 사용하면 필요없는 코드
