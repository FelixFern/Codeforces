n = int(input())
city = str(input())
if city[0] == "S" and city[len(city)-1] == "F":
    print("YES")
else:
    print("NO")