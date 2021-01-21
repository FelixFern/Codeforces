n = int(input())
data = []
count = 0
for i in range(n):
    h, a = map(int,input().split())
    data.append([h,a])

for i in range(n-1):
    for j in range(i+1, n):
        if data[i][0] == data[j][1]:
            count += 1
        if data[i][1] == data[j][0]:
            count += 1
print(count)