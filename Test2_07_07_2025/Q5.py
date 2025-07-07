price1 = float(input("Enter price of product 1: "))
price2 = float(input("Enter price of product 2: "))
price3 = float(input("Enter price of product 3: "))
price4 = float(input("Enter price of product 4: "))
price5 = float(input("Enter price of product 5: "))

total = price1 + price2 + price3 + price4 + price5
gst = total * 0.18
final_bill = total + gst

print(f"Total bill after adding 18% GST: {final_bill:.2f}")
