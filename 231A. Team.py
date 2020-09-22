n = int(input())
data = []
count = 0
for i in range(n):
    data.append(list(map(int,input().split())))
for i in range(len(data)):
    total = 0
    for j in data[i]:
        total += j
        if total > 1:
            count += 1
            break
print(count)