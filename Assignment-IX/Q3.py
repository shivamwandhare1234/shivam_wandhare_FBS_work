#Code_1
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)

# Example usage
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print(f"Reversed number: {reversed_num}")

#Code_2
def reverse_number(n, rev=0):
    # Base case
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse_number(n // 10, rev)

# Input from user
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)

print(f"Reversed number: {reversed_num}")

