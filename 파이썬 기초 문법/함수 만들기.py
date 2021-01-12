def add(a, b):
    c = a + b
    print(c)


add(3, 4)


def add(a, b):
    c = a + b
    return c


print(add(3, 4))

x = add(3, 2)
print(x)


def add_minus(a, b):  # 여러 개의 값을 반환할 수 있다.(C++은 한개만 반환 가능하다.)
    c = a + b
    d = a - b
    return c, d


print(add_minus(3, 2))  # 튜플로 반환한다.


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]

for x in a:
    if isPrime(x):
        print(x, end=' ')


