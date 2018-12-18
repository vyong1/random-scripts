def sumsum(n):
    '''
    Give a number n
    Add numbers from 1 to n
    Add even numbers from 1 to n
    Add odd numbers from 1 to n
    '''
    total = 0
    even = 0
    odd = 0
    for i in range (1, n + 1, 2):
        # 1 3 5 7 9 ... n
        total += i
        odd += i
    for j in range (0, n + 1, 2):
        # 0 2 4 6 8 ... n
        total += j
        even += j
    print("Total: ", total)
    print("Even: ", even)
    print("Odd: ", odd)

def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
    return fact
