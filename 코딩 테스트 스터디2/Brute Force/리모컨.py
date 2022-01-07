import sys
n = sys.stdin.readline().strip()
m = int(sys.stdin.readline())
num = []
cnt1 = 0
cnt2 = 0
if m:
    li = list(map(str, sys.stdin.readline().split()))
    for i in n:
        print(num)
        if i not in li:
            num.append(i)
            cnt2 += 1
            continue
        if len(li) == 10:
            num = 100
            break
        else:
            temp1 = int(i)
            temp2 = int(i)
            while(1):
                temp1 = temp1 - 1
                temp2 = temp2 + 1
                if temp1 < 0:
                    temp1 += 1
                if temp2 > 9:
                    temp2 -= 1
                if str(temp1) not in li:
                    num.append(str(temp1))
                    cnt2 += 1
                    break
                elif str(temp2) not in li:
                    num.append(str(temp2))
                    cnt2 += 1
                    break


    num = "".join(num)
    a = abs(int(n) - 100)
    b = abs(int(n) - int(num))

    cnt2 += b
    cnt1 += a
else:
    a = abs(int(n) - 100)

    cnt2 += len(n)
    cnt1 += a
print(min(cnt1, cnt2))

