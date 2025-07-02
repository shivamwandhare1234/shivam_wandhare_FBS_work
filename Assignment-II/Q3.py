feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))

total_inches = (feet * 12) + inches

total_cm = total_inches * 2.54

meters = int(total_cm // 100)
centimeters = total_cm % 100

print("Distance =", meters, "meters and", centimeters, "centimeters")

