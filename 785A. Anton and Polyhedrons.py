n = int(input())
total = 0 
for i in range(n):
    faces = str(input())
    if faces == "Tetrahedron":
        total += 4
    elif faces == "Cube":
        total += 6
    elif faces == "Octahedron":
        total += 8
    elif faces == "Dodecahedron":
        total += 12
    elif faces == "Icosahedron":
        total += 20

print(total)