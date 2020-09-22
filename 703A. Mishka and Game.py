n = int(input())
score = []
mishka = 0
chris = 0
for i in range(n):
    score.append(list(map(int, input().split())))
for i in range(len(score)):
    mishka += score[i][0]
    chris += score[i][1]
if mishka == chris: 
    print("Friendship is magic!^^")
elif mishka > chris:
    print("Mishka")
else:
    print("Chris")