#Code_1
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def armstrong_sum(n, power):
    if n == 0:
        return 0
    return (n % 10) ** power + armstrong_sum(n // 10, power)

num = int(input("Enter a number: "))
digits = count_digits(num)
if armstrong_sum(num, digits) == num:
    print("Armstrong")
else:
    print("Not Armstrong")


#Code_2
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def armstrong_sum(n, digits):
    if n == 0:
        return 0
    return (n % 10) ** digits + armstrong_sum(n // 10, digits)

def is_armstrong(num):
    digits = count_digits(num)
    return num == armstrong_sum(num, digits)

# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

