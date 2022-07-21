n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(m): 
    s, t = map(int, input().split())
    fall = 0
    if s >= t: 
        for i in range(s-1, t-1, -1):
            if a[i] >= a[i-1]:
                fall += a[i] - a[i-1]
    else: 
        for i in range(s-1, t-1):
            if a[i] >= a[i+1]:
                fall += a[i] - a[i+1]
    print(fall)