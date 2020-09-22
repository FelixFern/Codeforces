n = int(input())
number = []

for i in range(n):
    number.append(int(input()))

for num in number:
    rounded = []
    count = 0
    for i in range(len(str(num))):
        x = str(num)
        if x[i] != '0':
            count += 1 
            rounded.append(int(x[i])*(10**(len(x)-i-1)))
    print(count)
    for i in range(len(rounded)):
        if i != (len(rounded)-1):
            print(rounded[i], end=" ")
        else:
            print(rounded[i])
