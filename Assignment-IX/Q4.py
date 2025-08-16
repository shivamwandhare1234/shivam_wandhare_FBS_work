#Code_1
def recursive_sum(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

# Example usage:
n = int(input("Enter a positive integer: "))
print("Sum of first", n, "numbers is:", recursive_sum(n))

#Code_2
def sum_n_numbers(n):
    # Base case
    if n == 0:
        return 0
    else:
        return n + sum_n_numbers(n - 1)

# Input from user
n = int(input("Enter a positive integer: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    total = sum_n_numbers(n)
    print(f"Sum of first {n} numbers is: {total}")
