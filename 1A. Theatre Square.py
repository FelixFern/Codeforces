import math

x, y, z = map(int, input().split())

theatreSquareArea = x * y
flagStone = z ** 2  
theatreSquareAreaF = 0 
flagStoneNeeded = 0

while theatreSquareAreaF <= theatreSquareArea :
    theatreSquareAreaF = flagStone * flagStoneNeeded
    if(theatreSquareAreaF >= theatreSquareArea):
        break
    flagStoneNeeded += 1

print(flagStoneNeeded)