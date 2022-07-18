t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    s = ['B' for i in range(m)]
    a = list(map(int, input().split()))
    for i in a: 
        if m-i < i-1:
            if s[m-i] == "B": 
                s[m-i] = "A"        
            elif s[m-i] == "A" and s[i-1] == "B":
                s[i-1] = "A"
        else: 
            if s[i-1] == "B": 
                s[i-1] = "A"        
            elif s[i-1] == "A" and s[m-i] == "B":
                s[m-i] = "A"
    for i in s:
        print(i, end='')
    print()
    