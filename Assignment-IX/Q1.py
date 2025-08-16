#Code_1

def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * fact(n-1)

def sum_fact(n):
    if n==0:
        return 0
    else:
        return fact(n) + sum_fact(n-1)

n = int(input("Enter a number to calculate the sum of factorials up to that number: "))
print(f"The sum of factorials from 0 to {n} is: {sum_fact(n)}")

#Code_2

def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * fact(n-1)

def sum_fact(n):
    total = 0
    for i in range(1, n + 1):
        total += fact(i)
    return total

n = int(input("Enter a number to calculate the sum of factorials up to that number: "))
print(f"The sum of factorials from 0 to {n} is: {sum_fact(n)}")



