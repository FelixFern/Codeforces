username = str(input())
splitted = [str (i) for i in username]
data = []
distinctCount = 0

for i in range(len(splitted)):
    if splitted[0] in data:
        splitted.remove(splitted[0])
    else:
        data.append(splitted[0])
        splitted.remove(splitted[0])
        distinctCount += 1

if distinctCount % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

