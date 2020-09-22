vowel = ["a", "o", "y", "e", "u", "i"]
x = str(input()).lower()
new = ""
for i in x:
    if i not in vowel:
        new += "." + i
print(new)