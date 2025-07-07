num = input("Enter a 3-digit number: ")

if len(num) == 3 and num.isdigit():
    first = int(num[0])
    second = int(num[1])
    third = int(num[2])

    if first == 2 * second and first * 2 == third:
        print("yes, you have done it.")
    else:
        print("please try next time.")
else:
    print("Invalid input. Please enter a 3-digit number.")