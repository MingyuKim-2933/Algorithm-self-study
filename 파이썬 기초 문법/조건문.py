x = 7
if 0 < x < 10:  # C나 C++과 다르게 파이썬만 가능
    print("10보다 작은 자연수")

x = 93
if x >= 90:  # 이 조건을 만족하기에 A만 출력한다.
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('B')
elif x >= 60:
    print('B')

if x >= 90:
    print('A')
if x >= 80:
    print('B')
if x >= 70:
    print('C')  # if문을 이어쓰면 각각 따로라서 93일때 모든 if문의 조건을 만족한다.
