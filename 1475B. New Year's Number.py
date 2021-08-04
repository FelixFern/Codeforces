t = int(input())
for i in range(t):
    n = int(input())
    if n < 2020 or n < 2021: 
        print("NO")
    elif n % 2020 == 0 or n % 2021 == 0:
        print("YES")
    else:
        x = n % 2020
        n -= x*2021
        if n < 0:
            n = -n
        n = str(n)
        if n == 0:
            print("YES")
        elif len(n) >= 4:
            if n == 0 or n[0] == n[2] and n[1] == n[3]:
                print("YES")
            else: 
                print("NO")
        else: 
            print("NO")