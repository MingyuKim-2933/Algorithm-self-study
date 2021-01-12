import random as r
a = []  # 빈 리스트를 생성한다.
print(a)
b =list()  # 빈 리스트를 생성한다.
print(b)

a = [1, 2, 3, 4, 5]
print(a)  # [1, 2, 3, 4, 5]

b = list(range(1, 11))
print(b)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = a+b  # 리스트를 합칠 수 있다.
print(c)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a.append(6)  # append() : 리스트에 인자의 값 추가
print(a)

a.insert(3, 7)  # insert()를 사용하면 2번째 인자의 값을 1번째 인자에 해당하는 index 위치에 삽입한다. index[3]자리에 7의 값 삽입
print(a)

a.pop()  # pop() 함수에 인자를 주지 않을 경우 제일 마지막 index의 값이 리스트에서 빠진다.
print(a)
a.pop(3)
print(a)  # 인자에 해당하는 index의 값이 리스트에서 빠진다.

a.remove(4)  # remove() 함수의 index 값이 아니라 해당하는 값을 찾아 리스트에서 삭제한다.
print(a)

print(a.index(5))  # index() 함수의 인자 값을 찾아 그 값의 index를 반환한다.

a = list(range(1, 11))
print(a)
print(sum(a))  # sum() : 모든 인자 값을 더해서 반환한다.
print(max(a))  # max()  : 인자 값 중 가장 큰 값을 반환한다.
print(min(a))  # min() : 인자 값 중 가장 작은 값을 반환한다.
r.shuffle(a)  # random을 import 하였을 때 shuffle()을 사용하면 list 값들을 무작위로 섞어서 반환한다.
print(a)
a.sort()  # sort() : 인자 값들을 오름차순으로 정렬하여 반환한다.
print(a)
a.sort(reverse=True)
print(a)  # sort(reverse=True) : 인자 값들을 내림차순으로 정렬하여 반환한다.(True대신 1을 써도 된다.)

a.clear()  # list안의 모든 값을 삭제하여 빈 리스트를 반환한다.
print(a)