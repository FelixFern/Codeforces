x = str(input())
count = 1
for i in range(len(x)-1):
    if count >= 7:
        break
    if x[i] == x[i+1]:
        count += 1
    else: 
        count = 1
        
if count < 7:
    print("NO")
else:
    print("YES")