t = int(input())
for i in range(t):
    count = 0
    a,b = map(int,input().split())
    if a % b == 0:
        print(count)
    else:
        print(b - a%b)