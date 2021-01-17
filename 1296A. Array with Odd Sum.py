n = int(input())

for i in range(n):
    a = int(input())
    x = list(map(int, input().split()))
    odd = 0
    even = 0 
    sums = 0
    for i in x:
        if i % 2 == 0:
            even += 1
        else: 
            odd += 1
        sums += i
    if (a % 2 == 0 and (odd >= 1 and even >= 1)) or sums % 2 != 0:
        print("YES")
    elif (a % 2 != 0 and (odd >= 1)) or sums % 2 != 0:
        print("YES")
    else:
        print("NO")

