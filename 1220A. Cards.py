x = int(input())
unarrange = str(input())
zCount = 0 
nCount = 0 
for i in range(len(unarrange)):
    if unarrange[i] == 'z':
        zCount += 1
    elif unarrange[i] == 'n':
        nCount += 1
for i in range(nCount):
    print(1, end=" ")        
for i in range(zCount):
    print(0, end=" ")