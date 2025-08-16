#Code_1
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

# Example: Print first 10 Fibonacci numbers
n = 10
fib_series = fibonacci(n)
print("Fibonacci series:", fib_series)

#Code_2
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input from user
terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=",")
