#Largest primeNumber factor of 600851475143
# Bad because it will go infinite if it is a prime
def factorise(n):
    primes = []
    i = 1
    while n > 1:
        i += 1
        if n % i == 0:
            primes.append(i)
            n = n / i
            i = 1
    return primes

print(factorise(600851475143))
