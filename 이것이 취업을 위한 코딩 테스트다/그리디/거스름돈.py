n = 1260
count = 0

# 내 풀이
while n != 0:
    if n >= 500:
        n -= 500
        count += 1
    elif 500 > n >= 100:
        n -= 100
        count += 1
    elif 100 > n >= 50:
        n -= 50
        count += 1
    else:
        n -= 10
        count += 1
print(count)

# 책의 풀이
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n // coin
    n %= coin
print(count)

