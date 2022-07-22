t = int(input())

for i in range(t):
    rating = int(input())
    result = ""
    if rating >= 1900:
        result = "Division 1"
    elif rating >= 1600:
        result = "Division 2"
    elif rating >= 1400: 
        result = "Division 3"
    else: 
        result = "Division 4" 
    print(result)