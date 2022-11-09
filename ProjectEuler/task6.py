
limit = 100
sumOfSquare = 0

for i in range(1, limit+1):
    sumOfSquare += i**2

squareOfSum = 0
for i in range(1, limit+1):
    sum = limit * ( limit + 1) / 2
    squareOfSum = sum ** 2

print(squareOfSum-sumOfSquare)