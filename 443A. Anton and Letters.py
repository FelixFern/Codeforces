n = str(input())
unique = []
count = 0
for i in n:
    if i == "," or i == "{" or i == "}" or i == " ":
        continue
    else:
        if i not in unique:
            unique.append(i)
            count += 1
print(count)