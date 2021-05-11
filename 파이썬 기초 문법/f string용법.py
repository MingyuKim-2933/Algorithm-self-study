import datetime

age = 26
name = 'mingyu'
print('제 나이는', age, '입니다.')
print('제 나이는 {} 입니다. 제 이름은 {}입니다.'.format(age, name))  # format 용법
print(f'제 나이는 {age} 입니다. 제 이름은 {name}입니다.')  # f string 용법

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}')

date = datetime.datetime.now()
print(date)
print(f'{date:%Y-%m-%d-%A}')

# 튜플에도 f string 용법 사용 가능
t = (10, 20, 2, 100)
print(f'{t[0]} X {t[1]} = {t[2]*t[3]}')

print(f'{"hello":<10}')
print(f'{"hello":>10}')
print(f'{"hello":^10}')

print(f'{"hello":!<10}')
print(f'{"hello":@>10}')
print(f'{"hello":#^10}')

print(f'{0.456789:0.2f}')  # 소수점 표현(반올림된다.)
