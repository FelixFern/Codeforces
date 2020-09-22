n = int(input())
data = list(map(int, input().split()))
switch = 0

for i in range(n):
    if data[i] == 0:
        continue
    else:
        print("Hard")
        switch = 1
        break

if switch == 0:
    print("Easy")
else:
    pass