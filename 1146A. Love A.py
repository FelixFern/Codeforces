s = str(input())
aCount = 0 
other = 0
for i in s:
    if i == "a":
        aCount +=1
    else:
        other+=1
while other >= aCount:
    other -= 1
print(aCount+other)
