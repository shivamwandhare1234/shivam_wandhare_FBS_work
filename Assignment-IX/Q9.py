#Code_1
def power(m, n):
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return m
    else:
        return m * power(m, n - 1)

# Input from user
m = int(input("Enter the base (m): "))
n = int(input("Enter the exponent (n): "))

result = power(m, n)
print(f"{m} to the power {n} is: {result}")
