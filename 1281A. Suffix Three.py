t = int(input())
sentence = []
for i in range(t):
    sentence.append(str(input()))
for i in sentence:
    if i[len(i)-1] == "o":
        print("FILIPINO")
    elif i[len(i)-1] == "u":
        print("JAPANESE")
    elif i[len(i)-1] == "a":
        print("KOREAN")
    else:
        pass