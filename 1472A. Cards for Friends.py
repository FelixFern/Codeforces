t = int(input())

for i in range(t):
    w,h,n = map(int, input().split())
    count = 1
    while count < n:
        if w % 2 == 0:
            w /= 2
            count *= 2
        if h % 2 == 0:
            h /= 2 
            count *= 2 
        if h % 2 != 0 and w % 2 != 0:
            break
    if count >= n:
        print("YES")
    else:
        print("NO")