x = int(input()) 
#1,2,3,4,5
moves = 0
while x != 0:
    if int(x / 5) != 0:
        moves += int(x/5)
        x -= 5 * int(x/5)
    elif int(x / 4) != 0:
        moves += int(x/4)
        x -= 4 * int(x/4)
    elif int(x / 3) != 0:
        moves += int(x/3)
        x -= 3 * int(x/3)
    elif int(x / 2) != 0:
        moves += int(x/2)
        x -= 2 * int(x/2)
    elif int(x / 1) != 0:
        moves += int(x/1)
        x -= 1 * int(x/1)
print(moves)