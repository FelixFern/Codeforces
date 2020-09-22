n, m = map(int, input().split())
s = list(map(str, input().split()))
t = list(map(str, input().split()))
q = int(input())
year = []
for i in range(q):
    year.append(int(input()))
for i in year:
    x, y = 0, 0 
    x = i % n - 1
    y = i % m - 1
    print(s[x],end="")
    print(t[y])

