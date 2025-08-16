#Code_1
def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

# Input from user
num = int(input("Enter a number: "))

if num < 0:
    num = -num   # handle negative numbers by converting to positive
total = sum_of_digits(num)

print(f"Sum of digits of {num} is: {total}")
