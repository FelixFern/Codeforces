#http://codeforces.com/contest/4/problem/c
n = int(input())
newName = []
database = []

for i in range(n): 
    newName.append(str(input()))
    if newName[i] in database:
        continue
    else:
        database.append(newName[i])    

