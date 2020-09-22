matrices = []
location = []
movesX = 0
movesY = 0
for i in range(5):
    matrices.append(list(map(int,input().split())))
for i in range(len(matrices)):
    for j in range(len(matrices[i])):
        if matrices[i][j] == 1:
            location.append(i+1)
            location.append(j+1)
            break
movesX = abs(location[0]-3)
movesY = abs(location[1]-3)
print(movesX+movesY)