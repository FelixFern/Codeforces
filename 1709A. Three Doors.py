t = int(input())

for i in range(t): 
    x = int(input())
    key = list(map(int, input().split())) 
    result = ""
    if key[x - 1] == 0:
        result = "NO"
    else: 
        result = "YES"
        curr = x 
        for i in range(3):
            if key[curr - 1] != 0: 
                x = curr 
                curr = key[curr - 1]
                key[x - 1] = 0
        for i in key:
            if i != 0: 
                result = "NO"
    print(result)