n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

passed = True

for i in range(n):
    if (i+1 in p) or (i+1 in q):
        continue
    else:
        passed = False
if passed:
    print("I become the guy.")
else: 
    print("Oh, my keyboard!")