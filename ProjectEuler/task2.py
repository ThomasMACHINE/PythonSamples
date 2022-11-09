

def fib(n):
    # a = b + a
    # b = a
    sequence = []
    a, b = 0, 1
    while a < n:
        sequence.append(a)
        a, b = b, a+b
    return sequence

nums = fib(4000000)

sum = 0
for i in nums:
    if i % 2 == 0:
        sum += i

print(sum)