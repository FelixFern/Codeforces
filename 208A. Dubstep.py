n = str(input())
dubstep = ["W", "U", "B"]
new = []
counter = 0
nonWub = False
for i in n:
    if i == dubstep[counter]:
        counter += 1
        new.append(i)
    elif i == dubstep[0]:
        counter = 1
        nonWub = True
        new.append(i) 
    else: 
        nonWub = True
        counter = 0
        new.append(i) 
    if counter == 3:
        for i in range(3):
            new.pop()
        counter = 0 
        if nonWub:
            new.append(" ")
            nonWub = False

for i in new:
    print(i, end="")
    