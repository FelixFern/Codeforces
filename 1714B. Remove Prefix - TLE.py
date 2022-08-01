t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    hashmap = {}
    target = []
    for i in range(n):
        if a[i] not in hashmap:
            hashmap[a[i]] = 1
        elif i in hashmap: 
            hashmap[a[i]] += 1         
            target.append(i)
    total = 0
    if target != []:
        for i in range(n):
            popped = a.pop(0)
            total += 1
            if popped in target:
                target.remove(popped)
            if target == []:
                break
    if target != []: 
        total = 0
    print(total)