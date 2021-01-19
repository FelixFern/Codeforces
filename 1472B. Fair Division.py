t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    sums = 0
    one = 0
    two = 0
    for i in data:
        sums += i
        if i == 1:
            one += 1
        else:
            two += 1
    if sums % 2 == 0:
        if one == two:
            print("YES")
        elif (2*two - one) % 2 == 0 and one != 0:
            print("YES")
        elif (one != 0 and two == 0) or (one == 0 and (two % 2 == 0)):
            print("YES")
        else: print("NO")
    else:
        print("NO")