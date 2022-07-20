t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = 0 
    if a == 0: 
        result = 1 
    else: 
        result = 2*b + a + 1
    print(result)