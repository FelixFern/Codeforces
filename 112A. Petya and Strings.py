x = str(input().lower())
y = str(input().lower())
difference = []
count = 0

while True:
    for i in range(len(x)):
        if x[i] != y[i]:
            difference.append(x[i])
            difference.append(y[i])
            break
    break

if len(difference) != 0:
    xInt = ord(difference[0])
    yInt = ord(difference[1])
    if xInt > yInt:
        count = 1
    else:
        count = -1
print(count)