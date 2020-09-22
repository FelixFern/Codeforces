x = input()
y = list(input().split())
switch = 0 
for i in range(5):
    #Suit Check
    if x[0] == y[i][0]:
        print("YES")
        switch = 1
        break
    #Number Check
    elif x[1] == y[i][1]:
        print("YES")
        switch = 1
        break
    else:
        continue
if switch == 0:
    print("NO")
else:
    pass
    