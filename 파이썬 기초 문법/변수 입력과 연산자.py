a, b = input("숫자를 입력하세요: ").split()  # 2, 3을 띄어쓰기로 분리해서 입력하면 split()에 의해 a랑 b에 각각 저장
print(a+b)  # 23    a, b는 string 형으로 입력된다.
a = int(a)  # int 형 변환
b = int(b)
print(a+b)  # 5

a, b = map(int, input("숫자를 입력하세요: ").split())  # map은 내장형 함수이고 2개의 인자를 받는다. int 형으로 입력된다.

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  # 몫
print(a % b)  # 나머지
print(a**b)  # 제곱
