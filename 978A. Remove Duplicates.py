n = int(input())
data = list(map(int, input().split()))
unique = []

while n != 0:
    if data[n-1] not in unique:
        unique.append(data[n-1])
        n -= 1
    else:
        data.remove(data[n-1])
        n -= 1

print(len(data))
for i in data:
    print(i, end=" ")