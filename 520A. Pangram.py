n = int(input())
text = str(input()).lower()
unique = []
count = 0
for i in text:
    if i not in unique:
        unique.append(i)
        count += 1
if count == 26:
    print("YES")
else: 
    print("NO")