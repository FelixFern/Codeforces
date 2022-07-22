t = int(input())

for i in range(t): 
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    same = 1
    result = -1
    for i in range(n-1):
        if same == 3:
            result = a[i-1] 
        if a[i] == a[i+1]: 
            same += 1
        else: 
            same = 1
    if same == 3:
        result = a[i-1] 
    print(result)