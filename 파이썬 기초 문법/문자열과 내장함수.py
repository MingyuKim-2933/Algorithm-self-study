msg = "It is Time"
print(msg.upper())  # upper() : 문자열을 전부 대문자로 바꿔준다.
print(msg.lower())  # lower() : 문자열을 전부 소문자로 바꿔준다.
tmp =msg.upper()
print(tmp)
print(tmp.find('T'))  # find() 인자로 받은 문자열 '시작점'의 index를 반환, 일치하는 문자열이 없으면 -1을 반환한다.
print(tmp.count('T')) # count() 인자로 받은 문자열의 개수를 반환, 일치하는 문자열이 없으면 0을 반환한다.
print(msg[:2])  # slice 기능: 0번부터 2번 전까지 = 0, 1 번 index까지의 문자열을 출력한다.
print(msg[3:5])  # 3번~4번 index까지의 문자열을 출력한다.
print(len(msg))  # len()함수는 문자열의 길이를 반환한다.

for i in range(len(msg)):
    print(msg[i], end='')
print()

for j in msg:
    print(j, end='')
print()

for x in msg:
    if x.isupper():  # isupper() 대문자이면 True을 반환한다.
        print(x, end='')
print()

for x in msg:
    if x.islower():  # isupper() 소문자이면 True을 반환한다.
        print(x, end='')
print()

for x in msg:
    if x.isalpha():  # isalpha()는 알파벳일때 True을 반환한다.
        print(x, end='')
print()

tmp='AZ'
for x in tmp:
    print(ord(x))  # ord()는 ASCII code의 문자를 인자로 받아 문자의 ASCII number를 반환한다. A=65, Z=90

tmp='az'
for x in tmp:
    print(ord(x))  # ord()는 ASCII code의 문자를 인자로 받아 문자의 ASCII number를 반환한다. a=97, z=122

tmp=65
print(chr(tmp))  # chr()는 ASCII number을 인자로 받아 대응되는 ASCII code의 문자를 반환한다.

