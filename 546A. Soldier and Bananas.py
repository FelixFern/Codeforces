k, n, w = map(int, input().split())
totalCost = 0
for i in range(1,w+1):
    totalCost += k*i
if n > totalCost:
    print(0)
else:
    print(totalCost - n)