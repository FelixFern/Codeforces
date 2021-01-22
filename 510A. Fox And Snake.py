n, m = map(int, input().split())
control = True
count = 0 

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print("#", end="")
    else:
        if control:
            for j in range(m):
                if j != m-1:
                    print(".", end="")
                else:
                    print("#", end="")
            control = False
        else: 
            for j in range(m):
                if j != 0:
                    print(".", end="")
                else:
                    print("#", end="")
            control = True
    print("")