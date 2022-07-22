t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = "YES"
    if n == 1:
        result = "YES"
    if n > 1: 
        odd_seq = a[0] % 2
        even_seq = a[1] % 2 
        for i in range(0, n, 2):
            if odd_seq != a[i] % 2:
                result = "NO"
        for i in range(1, n, 2): 
            if even_seq != a[i] % 2:
                result = "NO"
    print(result)
    