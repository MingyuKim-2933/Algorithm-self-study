# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입 확인법
a = 123
print(type(a))
b = 12.3456789123456789123456789  # 8byte에서 잘리면서 반올림된다.
print(b)
print(type(b))
c = "student"
print(type(c))

# 출력방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep=', ')  # sep을 사용하면 print문의 출력할 것이 쉼표로 구분될 때마다 sep에 대입된 문자열을 뒤에 붙여서 출력함
print(a, b, c, sep='')
print(a, b, c, sep='\n')
# print(a, ) # end를 사용하면 print()를 해도 줄 바꿈을 하지 않고 변수 뒤에 end에 대입되는 것이 출력됨
# print(b, end=' 'end=' ')
# print(c)
