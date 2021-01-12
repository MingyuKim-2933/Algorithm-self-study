a= [23, 12, 36, 53, 19]
print(a[:3])  # index 0부터 2까지 출력
print(a[1:4])  # index 1부터 3까지 출력
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a):  # enumerate() 함수를 사용하면 index와 대응되는 값을 튜플형태(소괄호)로 반환한다.
    print(x)

b = (1, 2, 3, 4, 5)  # 튜플로 선언된다. 튜플은 리스트와 다르게 절대 수정할 수 없다.
print(b[0])
# b[0] = 7 튜플이라 이렇게 수정이 불가능하다.

for x in enumerate(a):
    print(x[0], x[1])  #튜플이 아닌 int 형으로 출력된다.
print()

for index, value in enumerate(a):  # index와 value를 선언하며 사용할 수 있는 방법. 가장 많이 사용된다.
    print(index, value)
print()

if all(60 > x for x in a):  # all()은 모든 조건이 참이 될 때 True를 반환한다.
    print("YES")
else:
    print("NO")

if any(15 > x for x in a):  # any()은 조건 중 하나라도 참이 되면 True를 반환한다.
    print("YES")
else:
    print("NO")