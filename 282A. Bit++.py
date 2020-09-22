n = int(input())
count = 0
operation = []

for i in range(n):
    operation.append(input())

for i in operation:
    if i[1] == '+' :
        count += 1
    else:
        count -= 1
print(count)