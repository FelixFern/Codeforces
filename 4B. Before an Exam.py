#http://codeforces.com/contest/4/problem/b
#Variable
d, sumTime = map(int, input().split())
minTime = []
maxTime = []
timeList = []
maxSum = 0
minSum = 0

for i in range(d):
    minTime.append(0)
    maxTime.append(0)
    minTime[i], maxTime[i] = map(int, input().split())
    maxSum += maxTime[i]
    minSum += minTime[i]

if maxSum >= sumTime >= minSum:
    timeList = minTime
    i = 0
    while minSum != sumTime:
        if minTime[i] != maxTime[i]:
            minSum += 1
            timeList[i] += 1
            if timeList[i] == maxTime[i]:
                i += 1
            else:
                continue
        else:
            i += 1
    print("YES")
    print(*timeList)
else:
    print("NO")
