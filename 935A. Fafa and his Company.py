x = int(input())
count = 0

for i in range(1, x): 
    if x - i == 0:
        pass
    elif (x - i) % i == 0:
        count += 1
    else: 
        continue
print(count)