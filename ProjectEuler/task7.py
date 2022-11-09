def findPrime(n):
    i = 2
    while i < n/2 + 1:
        if n % i == 0:
            return False
        i += 1
    return True

limit = 10001
numOfPrime = 0
counter = 2
while numOfPrime < limit:
    if findPrime(counter):
        numOfPrime += 1
        if(numOfPrime == limit):
            print(counter)
    
    counter += 1