def canBeDivided(num, limit):
    for i in range(1, limit + 1):
        if num % i != 0:
            return False
    return True

found = False
limit = 20
i = limit
while found == False:
    i += limit
    if canBeDivided(i, limit):
        print(i)
        found = True 