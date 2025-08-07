def print_factors(n):
    """Prints the factors of the given number n."""
    print(f"Factors of {n}:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

n=int(input("Enter a number to find its factors: "))
print_factors(n)