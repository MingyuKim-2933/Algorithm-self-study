from collections import namedtuple

# immutable 설명
l = [10, 20, 30]
t = (l, 10, 20)
print(t)
l[2] = 100  # 값은 변할 수 있다.
print(t)

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)  # instantiate with positional or keyword arguments

print(p)
print(p.x, p.y)
print(p[0] + p[1])  # 33이 출력된다. indexable like the plain tuple(11, 22)

# p[x]  # 이렇게는 사용할 수 없다.

i, j = p
print(i, j)

d = {
    'x': 100,
    'y': 200
}
p = Point(**d)  # **을 사용하면 dictionary를 넣을 수 있고 *은 튜플이나 리스트를 넣을 수 있다.

print(dir(Point))
print(p.x, p.y)

print(p._asdict())  # OrderedDictionary로 출력한다.

print(p._fields)  # 필드 출력

re_p = p._replace(x=1000)
print(re_p)
print(p)  # p는 변경되지 않는다.

print(p.index(100), p.index(200))  # index를 반환한다.
print(p.count(100))  # value의 개수를 반환한다.

from dataclasses import dataclass  # python 3.7부터 사용 가능, 구조체 import dataclass

@dataclass
class Point:
    x: int = None  # key와 value, value의 타입을 줄 수 있다.
    y: int = None

print(Point())

p = Point(10, 20)
print(p)

# i, j = p  # error .

print(p.x, p.y)

print(dir(p))

# 예제
기술명세 = namedtuple('기술', '기술이름, 자격증, 연차')  # csv 파일을 가지고 올 때 유용하다.
김민규 = 기술명세('파이썬', 'SQLD', '1')
print(김민규)
