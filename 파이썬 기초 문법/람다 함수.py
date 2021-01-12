def plus_one(x):
    return x+1

print(plus_one(1))

plus_two = lambda x: x+2
print(plus_two(1))

a = [1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))  # 람다 함수는 함수의 이름을 지정하지 않고 사용할 수 있어 편하다. sort algorithm에 주로 사용
