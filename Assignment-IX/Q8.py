#Code_1
def is_prime_recursive(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 1)

# Example usage:
num = int(input("Enter a number: "))
if is_prime_recursive(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")