a = range(10)  # range()는 순차적으로 정수 list를 만들어주는 함수
print(a)  # range 클래스를 출력한다.
print(type(a))  # range 자료형이다.
print(list(a))  #list로 출력해야 0부터 9까지의 정수를 출력한다.

b = range(1, 10)
print(list(b))

for i in range(10):
    print(i)  # 0~9까지 출력

for i in range(1, 11):
    print(i)  # 1~10까지 출력

for i in range(10, 0, -1):  # 하나씩 작아지게 하려면 range에 -1 인자를 추가해야 함  마지막 인자는 작아지거나 커지는 간격
    print(i)  # 10~1까지 출력

for i in range(1, 11):
    print(i)
    # if i == 5:
    #     break
else:
    print(11)  # for-else 구문 : 중간에 break로 종료되면 else문을 실행하지 않고 정상적으로 for문이 종료되면 else문을 실행한다.
