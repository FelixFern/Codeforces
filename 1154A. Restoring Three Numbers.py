a = list(map(int,input().split()))
maks = 0
def biggest(data, maks):
    minus = []
    for i in data:
        if i >= maks:
            maks = i
        else:
            continue
    for i in data:
        if i != maks:
            minus.append(i)
        else:
            continue
    for i in minus:
        print(maks - i, end=" ")

biggest(a, maks)
