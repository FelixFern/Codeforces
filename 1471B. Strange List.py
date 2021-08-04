t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    data = list(map(int,input().split()))
    added = []
    cont = True
    sums = 0
    for i in data: 
        if i % x == 0:
            added.append([i/x, x])
        else:
            cont = False
            break
    if cont:
        y = 0 
        while True:
            if added[y][0] % x == 0:
                added.append([added[y][0]/x, added[y][1]*x])
                y += 1
            else:
                break

    for i in range(len(added)):
        sums += added[i][0] * added[i][1]
    for i in data:
        sums += i
    print(int(sums))