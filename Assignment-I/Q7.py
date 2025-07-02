
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


Dis = b**2 - 4*a*c

# Calculate the roots
root1 = (-b + Dis**0.5) / (2*a)
root2 = (-b - Dis**0.5) / (2*a)

# Output the roots
print(f"Root1 = {root1}")
print(f"Root2 = {root2}")
