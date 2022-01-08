import sys
from collections import Counter

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort()


# count로 풀이하니 시간초과 발생..
# for i in li:
#     count.append(li.count(i))
#
# for cnt, value in enumerate(count):
#     if value == max(count):
#         if li[cnt] in temp:
#             pass
#         else:
#             temp.append(li[cnt])

count = Counter(li).most_common(2)  # Counter의 most_common()은 최빈값 개수 구함 파라미터는 구할 개수를 받고 (num, count) 튜플을 반환
print(round(sum(li)/n))
print(li[(n-1) // 2])

if len(count) >= 2:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

print(li[-1] - li[0])
