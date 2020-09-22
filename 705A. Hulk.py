n = int(input())
for i in range(n):
    if i+1 != n:
        if i % 2 == 0:
            print("I hate", end=" that ")
        else:
            print("I love", end=" that ")
    else:
        if i % 2 == 0:
            print("I hate", end=" it")
        else:
            print("I love", end=" it")