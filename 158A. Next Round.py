n, k = map(int, input().split())
a = list(map(int, input().split()))
total = k 
for i in range(0, n):
    if a[0] < 1:
        total = 0 
        break
    if i < k:
        if a[i] < 1:
            total -=1
    elif i >= k:
        if a[i] < 1:
            break
        if a[i] == a[k-1]:
            total +=1
        else:
            break
print(total)