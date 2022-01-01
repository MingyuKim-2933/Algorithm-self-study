import sys
n, k = map(int, sys.stdin.readline().split())
li = [i for i in range(1, n//2+1) if not n % i]
li.append(n)

print(li[k-1]) if len(li) >= k else print("0")
