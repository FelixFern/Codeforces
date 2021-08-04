t = int(input())
for i in range(t):
    x = int(input())
    cek = False
    if x % 2 == 1:
        print("YES")
    else: 
        for i in range(3, int(x**0.5/2), 2):
            if x % i == 0:
                cek = True
                break
        if cek:
            print("YES")
        else: 
            print("NO")