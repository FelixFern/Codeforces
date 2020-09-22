n = int(input())
words = []
for i in range(n):
    words.append(input())
for i in words:
    newWords = ""
    if len(i) > 10:
        newWords = i[0], str(len(i)-2), i[-1]
        print("".join(newWords))
    else:
        print(i)
