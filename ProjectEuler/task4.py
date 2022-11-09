'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(num):
    revNum = str(num)[::-1]
    return revNum == str(num)


max = 0

for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        if isPalindrome(product) and product > max:
            max = product

print(max)
