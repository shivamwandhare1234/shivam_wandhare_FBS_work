def print_z_pattern(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print(' ' * (n - i - 1) + '*')

# Example usage:
n = int(input("Enter the size of the Z pattern: "))
print_z_pattern(n)
