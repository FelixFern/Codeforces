#http://codeforces.com/problemset/problem/339/A
equation = list(map(int, input().split('+')))

def sort(data):
    size = len(data)
    key = 1
    start = 1
    while start < size:
        if start == 0: 
            start = key 
        if data[start] < data[start-1]: 
            data[start], data[start-1] = data[start-1], data[start]
            key = start
            start -= 1
        else:
            start += 1 
sort(equation)
if len(equation) > 1:
    for i in range(len(equation)-1):
        print(equation[i], end="+")
    print(equation[len(equation)-1])
else:
    print(equation[0])